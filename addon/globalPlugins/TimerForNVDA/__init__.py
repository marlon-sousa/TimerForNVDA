from .guiHelper import HideDialog, TimerDialog, dialogIsRunning
import globalPluginHandler
import gui
from scriptHandler import script
from .timer import getStatus, timer
import ui
import wx


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    @script(gesture="kb:NVDA+control+shift+t")
    def script_showTimerDialog(self, gesture):
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

    @script(gesture="kb:NVDA+control+shift+s")
    def script_activateTimer(self, gesture):
        if timer.isRunning():
            timer.stop()
        else:
            timer.start()

    @script(gesture="kb:NVDA+control+shift+p")
    def script_toggleTimer(self, gesture):
        timer.toggleOperation()

    @script(gesture="kb:NVDA+control+shift+r")
    def script_reportStatus(self, gesture):
        ui.message(getStatus())
