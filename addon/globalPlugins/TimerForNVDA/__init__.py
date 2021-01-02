from .guiHelper import TimerDialog
import globalPluginHandler
import gui
from scriptHandler import script
from .timer import getStatus, timer
import ui
import wx
import versionInfo


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    @script(gesture="kb:NVDA+control+shift+t")
    def script_showTimerDialog(self, gesture):
        def run():
            gui.mainFrame.prePopup()
            d = TimerDialog(gui.mainFrame)
            d.ShowModal()
            gui.mainFrame.postPopup()
        wx.CallAfter(run)

    @script(gesture="kb:NVDA+control+shift+s")
    def script_activateTimer(self, gesture):
        if timer.isRunning():
            timer.stop()
        else:
            timer.startTimer()

    @script(gesture="kb:NVDA+control+shift+p")
    def script_toggleTimer(self, gesture):
        timer.toggleOperation()

    @script(gesture="kb:NVDA+control+shift+r")
    def script_reportStatus(self, gesture):
        ui.message(getStatus())
