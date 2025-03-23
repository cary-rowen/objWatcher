# objWatcher add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Copyright (C) 2023 hwf1324 <1398969445@qq.com>

import addonHandler
import config
import gui
from gui import guiHelper
from gui import nvdaControls

import wx
import wx.adv


addonHandler.initTranslation()


class ObjWatcherPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: This is the label for the ObjWatcher settings panel.
	title = _("ObjWatcher")

	def makeSettings(self, settingsSizer):
		settingsSizerHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: This is the label of a SpinCtrl in the ObjWatcher settings panel
		# This option controls the interval of the Watcher timer (in milliseconds)
		intervalLabelText = _("Watcher timer interval")
		self.intervalEdit = settingsSizerHelper.addLabeledControl(
			intervalLabelText,
			nvdaControls.SelectOnFocusSpinCtrl,
			min=10, max=500,
			initial=int(config.conf["objWatcher"]["interval"])
		)

		self._appendWatchAttributesList(settingsSizerHelper)

	def _appendWatchAttributesList(self, settingsSizerHelper: guiHelper.BoxSizerHelper) -> None:
		self.watchAttributesList: wx.adv.EditableListBox = wx.adv.EditableListBox(
			self,
			label=_("Watch attributes"),
		)
		self.watchAttributesList.SetStrings(config.conf["objWatcher"]["watchAttributes"].split(","))
		editBtn: wx.BitmapButton = self.watchAttributesList.GetEditButton()
		editBtn.SetLabel(editBtn.GetToolTipText())
		newBtn: wx.BitmapButton = self.watchAttributesList.GetNewButton()
		newBtn.SetLabel(newBtn.GetToolTipText())
		delBtn: wx.BitmapButton = self.watchAttributesList.GetDelButton()
		delBtn.SetLabel(delBtn.GetToolTipText())
		upBtn: wx.BitmapButton = self.watchAttributesList.GetUpButton()
		upBtn.SetLabel(upBtn.GetToolTipText())
		downBtn: wx.BitmapButton = self.watchAttributesList.GetDownButton()
		downBtn.SetLabel(downBtn.GetToolTipText())

		settingsSizerHelper.addItem(self.watchAttributesList)

	def onSave(self):
		config.conf["objWatcher"]["interval"] = self.intervalEdit.Value
		config.conf["objWatcher"]["watchAttributes"] = ",".join(self.watchAttributesList.GetStrings())
