from .guiHelper import FastTimerDialog
import globalPluginHandler
import gui
from scriptHandler import script
import ui
import wx
import versionInfo


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    @script(gesture="kb:NVDA+control+n")
    def script_announceNVDAVersion(self, gesture):
        def run():
            gui.mainFrame.prePopup()
            d = FastTimerDialog(gui.mainFrame)
            d.ShowModal()
            gui.mainFrame.postPopup()
        wx.CallAfter(run)
        ui.message(versionInfo.version)
