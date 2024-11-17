# objWatcher add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Copyright (C) 2023 Cary-rowen <manchen_0528@outlook.com>
# Copyright (C) 2023 hwf1324 <1398969445@qq.com>

import addonHandler
import api
import config
import globalPluginHandler
import gui
import ui
import versionInfo
import wx
import tones
from scriptHandler import script
import time
from typing import Dict, Any, List
from functools import wraps
from logHandler import log

from . import cues
from . import settings

confspec = {
	"interval": "integer(default=100)",
	# TODO: Refactor hardcoded default watch attributes (Issue #6): https://github.com/cary-rowen/objWatcher/issues/6
	"watchAttributes": "string(default='name,value,description')",
}
config.conf.spec["objWatcher"] = confspec

addonHandler.initTranslation()


def finally_(func, final):
	"""Calls final after func, even if it fails."""

	def wrap(f):
		@wraps(f)
		def new(*args, **kwargs):
			try:
				func(*args, **kwargs)
			finally:
				final()

		return new

	return wrap(final)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: The category name displayed in the input gesture dialog
	scriptCategory = _("objWatcher")

	def __init__(self):
		super().__init__()
		self.watchingObjs: List[Dict[str, Any]] = []
		self.lastCheckedNumber = None
		self.lastKeyTime = 0
		self.lastKeyName = None
		self.timer = wx.Timer(gui.mainFrame)
		gui.mainFrame.Bind(wx.EVT_TIMER, self.onTimerEvent)
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(settings.ObjWatcherPanel)
		self.toggling = False
		self.watchingPaused = False

		# Define gesture bindings for the watcher layer commands
		self.__watcherGestures = {
			"kb:escape": "ExitLayer",
			"kb:delete": "DeleteLastChecked",
			"kb:t": "ToggleWindow",
			"kb:p": "TogglePause",
		}

		# Add number key bindings
		for numberKey in range(0, 10):
			self.__watcherGestures[f"kb:{numberKey}"] = "HandleNumberKey"

	def getScript(self, gesture):
		if not self.toggling:
			return globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		script = globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		if not script:
			# If an unbound key is pressed in layer mode, emit a beep and exit the layer mode
			tones.beep(120, 100)
			self.finish()
			return lambda *args, **kwargs: None
		return finally_(script, lambda: None)  # Do not automatically exit layer mode

	def finish(self):
		self.toggling = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_error(self, gesture):
		tones.beep(120, 100)

	@script(
		# Translators: Help message when entering objWatcher layer command in input help
		description=_("Enter watcher layer commands"),
		gesture="KB:NVDA+alt+w",
	)
	def script_watcherLayer(self, gesture):
		if self.toggling:
			self.script_error(gesture)
			return

		# Generate concise status summary with rephrased messages
		watched_count = len(self.watchingObjs)
		summary_message = (
			# Translators: Message when watching has not started and no items are in the watch list
			_("No items are being watched. Please add items to watch.")
			if watched_count == 0
			# Translators: Message when watching is active and items are being watched
			else _("Watching in progress. {} items are being tracked.").format(watched_count)
			if not self.watchingPaused
			# Translators: Message when watching is paused and items are in the watch list
			else _("Watching paused. {} items in the watch list.").format(watched_count)
		)
		ui.message(summary_message)
		self.bindGestures(self.__watcherGestures)
		self.toggling = True
		tones.beep(100, 10)

	def script_ExitLayer(self, gesture):
		self.finish()
		# Translators: Message when exiting watcher layer
		ui.message(_("Exited watcher layer"))

	@script(
		# Translators: Presented in input help mode.
		description=_("Add current navigator object to watchlist"),
	)
	def script_HandleNumberKey(self, gesture):
		# Get the pressed number (0-9)
		try:
			number = int(gesture.mainKeyName) if gesture.mainKeyName != "0" else 10
		except ValueError:
			invalid_key = gesture.mainKeyName
			log.warning(f"Invalid key detected: '{invalid_key}'.")
			# Translators: Message to the user when an invalid gesture is detected
			ui.message(
				_("Invalid key: '{}'. Please use a numeric key like NVDA+Alt+0~9.").format(invalid_key)
			)
			return

		# Check if this number is already being watched
		for data in self.watchingObjs:
			if data.get("number") == number:
				# Record the last checked number
				self.lastCheckedNumber = number
				# Translators: Announces the status of the watched object at the given position
				ui.message(
					_("Position {}: {}").format(
						number,
						# Ensure lastText is populated before comparison
						data["name"]
						if data["name"] == (data["lastText"] or self._getWatchingAttribute(data["obj"]))
						# If name and lastText are different, report both name and lastText
						else "{} - {}".format(
							data["name"], data["lastText"] or self._getWatchingAttribute(data["obj"])
						)
						if data["name"]
						# If name is empty, only report lastText or fallback to _getWatchingAttribute
						else data["lastText"] or self._getWatchingAttribute(data["obj"]),
					)
				)
				return

		# If this number is not used, try to add the current object
		obj = api.getNavigatorObject()
		if not obj:
			# Translators: Message when there is no navigation object to add
			ui.message(_("No navigation object available to add"))
			self.finish()  # Exit layer mode on error
			return

		# Check if the object is already being watched at another position
		for data in self.watchingObjs:
			if obj == data["obj"]:
				existing_number = data.get("number")
				# Translators: Message when the object is already being watched at another position
				ui.message(_("This object is already being watched at position {}").format(existing_number))
				self.finish()  # Exit layer mode on error
				return

		# Add new object
		self.watchingObjs.append({
			"obj": obj,
			"lastText": None,
			"name": obj.name or _("Unnamed object"),
			"addTime": time.time(),
			"number": number,
		})

		# Start the timer if not paused and not already running
		if not self.watchingPaused and not self.timer.IsRunning():
			self.timer.Start(config.conf["objWatcher"]["interval"])

		if self.watchingPaused:
			# Translators: Message when an object is added to the watch list and watching not started
			ui.message(
				_("Added object to position {}: {}, Watching has not started.").format(
					number, self.watchingObjs[-1]["name"]
				)
			)
		cues.Start()
		self.finish()  # Exit layer mode after adding the object

	def _getMultiPressTimeout(self):
		try:
			nvda_version_year = versionInfo.version_year
			nvda_version_major = versionInfo.version_major
			if nvda_version_year > 2024 or (nvda_version_year == 2024 and nvda_version_major >= 4):
				timeout_ms = config.conf["keyboard"]["multiPressTimeout"]
			else:
				timeout_ms = 1000
		except Exception as e:
			log.warning("Failed to get multiPressTimeout from config: %s", e)
			timeout_ms = 1000
		return timeout_ms / 1000

	@script(
		# Translators: Presented in input help mode.
		description=_(
			"Press once to delete the last watched object; press twice to delete all watched objects"
		),
	)
	def script_DeleteLastChecked(self, gesture):
		currentTime = time.time()
		multiPressTimeout = self._getMultiPressTimeout()
		isDoublePress = (
			gesture.mainKeyName == self.lastKeyName and (currentTime - self.lastKeyTime) < multiPressTimeout
		)

		self.lastKeyTime = currentTime
		self.lastKeyName = gesture.mainKeyName

		if isDoublePress:
			# If delete key is pressed twice quickly, remove all watched objects
			if not self.watchingObjs:
				# Translators: Message when there are no objects being watched
				ui.message(_("No objects are being watched"))
				cues.NoObj()
				return

			count = len(self.watchingObjs)
			self.watchingObjs.clear()
			self.lastCheckedNumber = None
			if self.timer.IsRunning():
				self.timer.Stop()

			# Translators: Message when all watched objects have been removed
			ui.message(_("Removed all {} watched objects").format(count))
			self.finish()
			return

		if self.lastCheckedNumber is None:
			# Translators: Message when no object has been checked
			ui.message(_("No object has been checked"))
			return

		# Find and delete the object
		for data in self.watchingObjs:
			if data.get("number") == self.lastCheckedNumber:
				name = data["name"]
				number = self.lastCheckedNumber
				self.watchingObjs.remove(data)
				# Translators: Message when a watched object has been removed
				ui.message(_("Removed {} from position {}").format(name, number))

				# Stop the timer if there are no more objects being watched
				if not self.watchingObjs and self.timer.IsRunning():
					self.timer.Stop()

				self.lastCheckedNumber = None  # Reset the last checked number
				return

		# Translators: Message when the last checked object is no longer being watched
		ui.message(_("The last checked object is no longer being watched"))
		self.lastCheckedNumber = None

	def onTimerEvent(self, event):
		if self.watchingPaused:
			return  # Do nothing if watching is paused

		if not self.watchingObjs:
			self.timer.Stop()
			return

		# Use a copy of the list to avoid modifying the list while iterating
		for data in self.watchingObjs[:]:
			obj = data["obj"]
			try:
				# Check if the object still exists and is accessible
				if not api.isNVDAObject(obj):
					name = data["name"]
					self.watchingObjs.remove(data)
					# Translators: Message when an object is no longer available and has been removed
					ui.message(
						_("{} is no longer available and has been removed from watch list").format(name)
					)
					continue

				attributeText = self._getWatchingAttribute(obj)
				if data["lastText"] != attributeText:
					data["lastText"] = attributeText
					# Translators: Message announcing updated attributes of the object
					ui.message(_("{}").format(attributeText))
			except Exception:
				# If there is an error accessing object attributes, remove the object
				name = data["name"]
				self.watchingObjs.remove(data)
				# Translators: Message when an object caused an error and has been removed
				ui.message(_("{} caused an error and has been removed from watch list").format(name))

		# Stop the timer if all objects have been removed
		if not self.watchingObjs:
			self.timer.Stop()

	def _getWatchingAttribute(self, obj):
		"""Retrieve the watched attributes of an object"""
		non_empty_attributes = []
		seen_values = set()
		watch_attrs = config.conf["objWatcher"]["watchAttributes"].split(",")

		try:
			for attr in watch_attrs:
				if hasattr(obj, attr):
					value = getattr(obj, attr, None)
					if value and str(value) not in seen_values:
						non_empty_attributes.append(str(value))
						seen_values.add(str(value))
		except Exception:
			return _("Error reading attributes")

		return ", ".join(non_empty_attributes) if non_empty_attributes else ""

	def terminate(self):
		super().terminate()
		if self.timer:
			self.timer.Stop()
			self.timer.Destroy()
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(settings.ObjWatcherPanel)

	@script(
		# Translators: Presented in input help mode.
		description=_("Toggle the watch status of the current window"),
	)
	def script_ToggleWindow(self, gesture):
		obj = api.getForegroundObject()
		if not obj:
			# Translators: Message when there is no foreground window available
			ui.message(_("No foreground window available"))
			return

		# Check if the object is already in the watch list
		for data in self.watchingObjs:
			if obj == data["obj"]:
				name = data["name"]
				self.watchingObjs.remove(data)
				# Translators: Message when a window has been removed from the watch list
				ui.message(_("Removed window {} from watch list").format(name))
				if not self.watchingObjs and self.timer.IsRunning():
					self.timer.Stop()
				return

		# Add the object to the watch list
		self.watchingObjs.append({
			"obj": obj,
			"lastText": None,
			"name": obj.name or _("Unnamed window"),
			"addTime": time.time(),
			"number": None,  # Special objects do not use number positions
		})

		# Start the timer if not paused and not already running
		if not self.watchingPaused and not self.timer.IsRunning():
			self.timer.Start(config.conf["objWatcher"]["interval"])

		# Translators: Message when a window has been added to the watch list
		ui.message(_("Added window {} to watch list").format(self.watchingObjs[-1]["name"]))

	@script(
		# Translators: Presented in input help mode.
		description=_("Toggle pause/resume watching"),
	)
	def script_TogglePause(self, gesture):
		if self.watchingPaused:
			self.watchingPaused = False
			# Translators: Message when watching is resumed
			ui.message(_("Watching resumed"))
			cues.Start()
			# Start the timer if there are objects to watch and the timer is not running
			if self.watchingObjs and not self.timer.IsRunning():
				self.timer.Start(config.conf["objWatcher"]["interval"])
		else:
			self.watchingPaused = True
			# Translators: Message when watching is paused
			ui.message(_("Watching paused"))
			cues.Stop()
			# Stop the timer if it's running
			if self.timer.IsRunning():
				self.timer.Stop()
