from .guiHelper import TimerDialog
import globalPluginHandler
import gui
from scriptHandler import script
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
