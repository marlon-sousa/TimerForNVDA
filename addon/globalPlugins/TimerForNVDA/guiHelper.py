# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.


import config
import core
from enum import Enum, unique
import gui
import locale
from gui import guiHelper
from .timer import getStatus, reportWithSound, reportWithSpeech, timer
from .types import getOperationModes, getTimeUnits, TimerEvent
import string
import ui
import wx


class TimerDialog(wx.Dialog):
    """A dialog used to manager timer and stop watch.
    """

    def __init__(self, parent):
        # Translators: Title of a dialog to find text.
        super(TimerDialog, self).__init__(
            parent, wx.ID_ANY, _("Timer for NVDA"))

        # current operation mode
        self._operationMode = timer._mode
        self._timeUnit = timer._timeUnit

        self._buildGui()
        self._bindEvents()

    def _buildGui(self):
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainHelper = guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
        timerHelper = guiHelper.BoxSizerHelper(
            self, orientation=wx.HORIZONTAL)
        feedbackHelper = guiHelper.BoxSizerHelper(
            self, orientation=wx.HORIZONTAL)
        self._timerValueCtrl = timerHelper.addLabeledControl(
            self._getTimerConfigLabel(), wx.TextCtrl)
        self._timeUnitCTRL = timerHelper.addItem(wx.RadioBox(self, label=_(
            "Time unit"), choices=getTimeUnits(), majorDimension=1, style=wx.RA_SPECIFY_ROWS))
        mainHelper.addItem(timerHelper)
        self._operationModeCTRL = mainHelper.addLabeledControl(
            _("Type of watch"), wx.Choice, id=wx.ID_ANY, choices=getOperationModes())
        self._setDefaultValues()
        timerActions = guiHelper.ButtonHelper(wx.HORIZONTAL)
        self._startButton = timerActions.addButton(self, label=_("start"))
        self._pauseButton = timerActions.addButton(self, label=_("Pause"))
        self._stopButton = timerActions.addButton(self, label=_("stop"))
        mainHelper.addItem(timerActions)
        self._reportWithSoundCheckbox = feedbackHelper.addItem(
            wx.CheckBox(self, id=wx.ID_ANY, label=_("Report progress with sound")))
        self._reportWithSpeechCheckbox = feedbackHelper.addItem(
            wx.CheckBox(self, id=wx.ID_ANY, label=_("Report progress with speech")))
        mainHelper.addItem(feedbackHelper)
        dialogActions = guiHelper.ButtonHelper(wx.HORIZONTAL)
        self._okButton = dialogActions.addButton(self, label=_("Ok"))
        self._cancelButton = dialogActions.addButton(self, label=_("Cancel"))
        mainHelper.addItem(dialogActions)
        self._statusBar = wx.StatusBar(self, id=wx.ID_ANY)
        self._statusBar.SetStatusText(
            getStatus())
        mainHelper.addItem(self._statusBar, flag=wx.EXPAND)
        self._refreshUI()
        mainSizer.Add(mainHelper.sizer, border=10, flag=wx.ALL)
        mainSizer.Fit(self)
        self.SetSizer(mainSizer)
        self.CentreOnScreen()

    def _bindEvents(self):
        self._startButton.Bind(wx.EVT_BUTTON, self.OnStart)
        self._stopButton.Bind(wx.EVT_BUTTON, self.OnStop)
        self._pauseButton.Bind(wx.EVT_BUTTON, self.OnPause)
        self._timerValueCtrl.Bind(wx.EVT_CHAR, self.OnKeyPress)
        self._reportWithSoundCheckbox.Bind(
            wx.EVT_CHECKBOX, self.OnReportWithSoundChanged)
        self._reportWithSpeechCheckbox.Bind(
            wx.EVT_CHECKBOX, self.OnReportWithSpeechChanged)
        timer.registerReporter(self.OnTimer)

    def _setDefaultValues(self):
        self._timeUnitCTRL.SetSelection(self._getIndex(
            getTimeUnits(), timer._timeUnit.value))
        self._operationModeCTRL.SetSelection(self._getIndex(
            getOperationModes(), timer._mode.value))

    def _getIndex(self, items, item):
        for i, _ in enumerate(items):
            if items[i] == item:
                return i
        return -1

    def _refreshUI(self):
        self._startButton.Enable(not timer.isRunning(
        ) and self._timerValueCtrl.GetValue() != "")
        self._stopButton.Enable(timer.isRunning())
        self._pauseButton.Enable(timer.isRunning())
        self._operationModeCTRL.Enable(not timer.isRunning())
        self._timeUnitCTRL.Enable(not timer.isRunning())
        self._timerValueCtrl.SetEditable(not timer.isRunning())
        if not self._startButton.IsEnabled():
            self._stopButton.SetFocus()
        elif not self._stopButton.IsEnabled() and wx.Window.FindFocus() != self._timerValueCtrl:
            self._startButton.SetFocus()

    def OnKeyPress(self, evt):
        key = evt.GetKeyCode()
        character = chr(key)
        if key == 8 or key > 256 or character == locale.localeconv()["decimal_point"] or character in string.digits:
            wx.CallAfter(self._refreshUI)
            evt.Skip()

    def OnReportWithSoundChanged(self, evt):
        if evt.IsChecked():
            timer.registerReporter(reportWithSound)
        else:
            timer.unregisterReport(reportWithSound)

    def OnReportWithSpeechChanged(self, evt):
        if evt.IsChecked():
            timer.registerReporter(reportWithSpeech)
        else:
            timer.unregisterReport(reportWithSpeech)

    def OnStart(self, evt):
        timer.startTimer(int(self._timerValueCtrl.GetValue()), self._timeUnit)

    def OnStop(self, evt):
        timer.stop()

    def OnPause(self, evt):
        pass

    def OnTimer(self, evt):
        if evt["type"] in [TimerEvent.STARTED, TimerEvent.STOPPED]:
            self._refreshUI()
        self._statusBar.SetStatusText(
            getStatus())

    def _getTimerConfigLabel(self):
        return f"amount of {self._timeUnit.value} for {self._operationMode.value}"
