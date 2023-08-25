# objWatcher add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Copyright (C) 2023 Cary-rowen <manchen_0528@outlook.com>

import api
import addonHandler
import gui
import globalPluginHandler
import ui
import wx
from scriptHandler import script, getLastScriptRepeatCount
from . import cues

addonHandler.initTranslation()

WATCHER_TIMER_INTERVAL = 100  # milliseconds

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    # Translators: The category name displayed in the input gesture dialog
    scriptCategory = _("objWatcher")

    def __init__(self):
        super().__init__()
        self.watchingObj = None
        self.lastAttributeText = None
        self.timer = wx.Timer(gui.mainFrame)
        gui.mainFrame.Bind(wx.EVT_TIMER, self.onTimerEvent, self.timer)

    @script(
        description=_(
            # Translators: Input a help message in objWatcher about starting or stopping and reporting the currently watched attributes.
            "Press once to start watching the current navigator object. If a navigator object is currently being watched, the watched attribute will be reported. Press twice to stop watching."
        ),
        gesture="KB:NVDA+control+w"
    )
    def script_startOrStopWatcher(self, gesture):
        if not self.timer:
            return   
        if getLastScriptRepeatCount() > 0:
            if self.timer.IsRunning():
                self.timer.Stop()
                cues.Stop()
                # Translators: Messages reported when watcher is stopped
                ui.message(_("Stopped watcher"))
        else:
            if self.timer.IsRunning():
                ui.message(self._getWatchingAttribute())
            else:
                self.watchingObj = api.getNavigatorObject()     
                self.timer.Start(WATCHER_TIMER_INTERVAL)
                if self.watchingObj:
                    cues.Start()
                    # Translators: Messages reported when watcher is start.
                    ui.message(_("Started watcher {}").format(self._getWatchingAttribute()))
                else:
                    cues.NoObj()
                    # Translators: Messages reported when No navigation object available to watch.
                    ui.message(_("No navigation object available to watch"))

    def onTimerEvent(self, event):
        if not self.watchingObj:
            return
        attributeText = self._getWatchingAttribute()
        if self.lastAttributeText == attributeText:
            return
        self.lastAttributeText = attributeText
        ui.message(attributeText)

    def _getWatchingAttribute(self):
        non_empty_attributes = []
        seen_values = set()   
        for attr in ['name', 'value', 'description']:
            if hasattr(self.watchingObj, attr):
                value = getattr(self.watchingObj, attr)
                if value and value not in seen_values:
                    non_empty_attributes.append(value)
                    seen_values.add(value)    
        attribute_text = ', '.join(non_empty_attributes)
        return attribute_text

    def terminate(self):
        super().terminate()
        if self.timer:
            self.timer.Stop()
            self.lastAttributeText = None
            self.timer = None
            self.watchingObj = None

