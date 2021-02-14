# -*- coding: UTF-8 -*-
# A part of the TimerForNVDA addon for NVDA
# Copyright (C) 2021 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import addonHandler
from .guiHelper import HideDialog, TimerDialog, dialogIsRunning
import globalPluginHandler
import gui
from scriptHandler import script
from .timer import getStatus, timer
import ui
import wx

addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    scriptCategory = _("Timer for NVDA")

    def __init__(self):
        super(GlobalPlugin, self).__init__()
        self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
        self.timerForNVDAMenu = self.toolsMenu.Append(wx.ID_ANY, _(
            "Timer for NVDA settings"), _("Show settings dialog for Timer for NVDA addon"))
        gui.mainFrame.sysTrayIcon.Bind(
            wx.EVT_MENU, self.OnSettingsDialog, self.timerForNVDAMenu)

    def terminate(self):
        super(GlobalPlugin, self).terminate()

        try:
            self.toolsMenu.Remove(self.timerForNVDAMenu)
        except (RuntimeError, AttributeError):
            pass

    @ script(gesture="kb:NVDA+shift+t", description=_("Shows the timer for MVDA settings dialog"))
    def script_showTimerDialog(self, gesture):
        self.showSettingsDialog()

    def OnSettingsDialog(self, evt):
        self.showSettingsDialog()

    def showSettingsDialog(self):
        if dialogIsRunning():
            # script has been triggered when timer dialog is already shown.
            # we will hide it now to allow focus to be set at it when it is shown again
            HideDialog()
        else:
            self.dialog = TimerDialog(gui.mainFrame)

        def run():
            gui.mainFrame.prePopup()
            self.dialog.Show(True)
            gui.mainFrame.postPopup()
        wx.CallAfter(run)

    @ script(gesture="kb:NVDA+control+shift+s", description=_("Starts or stops timer or stopwatch"))
    def script_activateTimer(self, gesture):
        if timer.isRunning():
            timer.stop()
        else:
            timer.start()

    @ script(gesture="kb:NVDA+control+shift+p", description=_("Pauses or resumes a running timer or stopwatch"))
    def script_toggleTimer(self, gesture):
        timer.toggleOperation()

    @ script(gesture="kb:NVDA+control+shift+r", description=_("Obtains status report from time or stopwatch"))
    def script_reportStatus(self, gesture):
        ui.message(getStatus())
