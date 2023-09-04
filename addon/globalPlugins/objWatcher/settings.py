# objWatcher add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Copyright (C) 2023 hwf1324 <1398969445@qq.com>

import config
import gui
import wx
from gui import guiHelper


class ObjWatcherPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: This is the label for the ObjWatcher settings panel.
	title = _("ObjWatcher")

	def makeSettings(self, settingsSizer):
		settingsSizerHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: This is the label of a SpinCtrl in the ObjWatcher settings panel
		# This option controls the interval of the Watcher timer (in milliseconds)
		intervalSpinCtrlLabel = _("Watcher timer interval")
		self.intervalSpinCtrl = settingsSizerHelper.addLabeledControl(intervalSpinCtrlLabel, wx.SpinCtrl)
		self.intervalSpinCtrl.SetValue(config.conf["objWatcher"]["interval"])

	def onSave(self):
		global interval
		interval = config.conf["objWatcher"]["interval"] = self.intervalSpinCtrl.GetValue()
