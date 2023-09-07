# objWatcher add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Copyright (C) 2023 hwf1324 <1398969445@qq.com>

import addonHandler
import config
import gui
from gui import guiHelper
from gui import nvdaControls

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

	def onSave(self):
		config.conf["objWatcher"]["interval"] = self.intervalEdit.Value
