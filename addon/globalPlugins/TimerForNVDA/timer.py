# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.


from . import conf
import core
from logHandler import log
import nvwave
import os
import threading
import time
import tones
from .types import getSingularTimeUnit, getTime, OperationMode, TimeUnit, TimerEvent, TimerStatus
import wx
import ui

timerRunning = False

timer = None


class Timer:

    def __init__(self):
        self._resetState()
        self._initialTime = None
        self.stopWatchResult = None
        self._running = False
        self._shouldRun = False
        self._thread = None
        self._mode = OperationMode[conf.getConfig("operationMode")]
        self._timeUnit = TimeUnit[conf.getConfig("timeUnit")]
        self._reporters = []
        self._counterLock = threading.Lock()

    def _resetState(self):
        self._currentTime = 0
        self._targetTime = 0
        self._status = TimerStatus.STOPPED
        self._message = ""

    def registerReporter(self, func):
        for f in self._reporters:
            if f == func:
                return
        self._reporters.append(func)

    def unregisterReporter(self, func):
        try:
            self._reporters.remove(func)
        except:
            pass

    def getTimeUnit(self):
        return self._timeUnit.name

    def getMode(self):
        return self._mode.name

    def isRunning(self):
        return not self._status == TimerStatus.STOPPED

    def isPaused(self):
        return self._status == TimerStatus.PAUSED

    def reportStatus(self, func):
        func(self._currentTime, self._targetTime, self._timeUnit, self._mode)

    def isTimer(self):
        return self._mode == OperationMode.TIMER

    def isStopWatch(self):
        return self._mode == OperationMode.STOP_WATCH

    def setTimeUnitFromValue(self, value):
        if not self.isRunning():
            self._timeUnit = TimeUnit(value)

    def _startTimer(self, initialTime=None):
        if self._shouldStart(initialTime):
            self._status = TimerStatus.STARTED
            # save initialTime if provided
            # this is useful because if we are starting timer dialogless we will reuse last initial time configured
            if initialTime:
                self._initialTime = initialTime
            self._currentTime = self._initialTime
            self._run()
            self._report(TimerEvent.STARTED)

    def _startStopWatch(self):
        if self._shouldStart():
            self._status = TimerStatus.STARTED
            self._run()
            self._report(TimerEvent.STARTED)

    def start(self, initialTime=None):
        if(self.isTimer()):
            self._startTimer(initialTime)
        else:
            self._startStopWatch()

    def toggleOperation(self):
        if self.isPaused():
            self.resume()
        else:
            self.pause()

    def pause(self):
        if self._thread is None or not self.isRunning():
            self.warn(_("can not pause timer because it is not running"))
            return
        self._shouldRun = False
        if self._thread != threading.current_thread() and self._thread.is_alive():
            self._thread.join()
        self._status = TimerStatus.PAUSED
        self._report(TimerEvent.PAUSED)

    def resume(self):
        if not self.isPaused():
            self.warn(_("Can not resumer because timer is not paused"))
            return
        self._status = TimerStatus.STARTED
        self._run()
        self._report(TimerEvent.RESUMED)

    def stop(self):
        if self._thread is None:
            return
        self._shouldRun = False
        if self._thread != threading.current_thread() and self._thread.is_alive():
            self._thread.join()
        if self.isStopWatch():
            self.stopWatchResult = self._counter
            self._report(TimerEvent.COMPLETED)
        self._report(TimerEvent.STOPPED)
        self._resetState()

    def _run(self):
        self._shouldRun = True
        self._thread = threading.Thread(
            target=(self._timer if self.isTimer() else self._stopWatch))
        self._thread.start()

    def warn(self, warning):
        self._message = warning
        self._report(TimerEvent.WARNING)

    def _shouldStart(self, initialTime=None):
        if self.isTimer() and not initialTime and not self._initialTime:
            self.warn(_("Initial time not configured. starting aborted"))
            return False
        return self._thread is None or self._thread and not self._thread.is_alive()

    def _shouldStop(self):
        return not self._shouldRun

    def _incrementCurrentTime(self):
        with self._counterLock:
            self._currentTime = self._currentTime + 1

    def _decrementCurrentTime(self):
        with self._counterLock:
            self._currentTime = self._currentTime - 1

    def _report(self, evt):
        for reporter in self._reporters:
            wx.CallAfter(reporter, {
                "type": evt,
                "currentTime": self._currentTime,
                "timeUnit": self._timeUnit.value,
                "watchType": self._mode.value,
                "message": self._message,
                "status": self._status,
            })

    def _timer(self):
        self._targetTime = 0
        self._counter = self._currentTime * getTime(self._timeUnit)
        while self._counter > self._targetTime:
            if self._shouldStop():
                break
            time.sleep(1)
            self._counter -= 1
            self._report(TimerEvent.COUNTER)
            if self._counter % getTime(self._timeUnit) == 0:
                self._decrementCurrentTime()
                self._report(TimerEvent.TICK)
            if self._currentTime == 0:
                self._report(TimerEvent.COMPLETED)
                self.stop()
                break

    def _stopWatch(self):
        self._counter = self._currentTime * getTime(self._timeUnit)
        while True:
            if self._shouldStop():
                break
            time.sleep(1)
            self._counter += 1
            self._report(TimerEvent.COUNTER)
            if self._counter % getTime(self._timeUnit) == 0:
                self._incrementCurrentTime()
                self._report(TimerEvent.TICK)


beepDurations = {
    TimeUnit.SECONDS.value: 10,
    TimeUnit.MINUTES.value: 100,
    TimeUnit.HOURS.value: 200
}


def getSoundsPath():
    soundsPath = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "..", "..", "sounds")
    return soundsPath


def playAlarm():
    nvwave.playWaveFile(os.path.join(getSoundsPath(), "timer.wav"))


def reportWithSpeech(evt):
    if evt["type"] == TimerEvent.TICK and evt["currentTime"] != 0:
        ui.message(str(evt["currentTime"]))


def reportWithSound(evt):
    if evt["type"] == TimerEvent.TICK and evt["currentTime"] != 0:
        tones.beep(4000, beepDurations[evt["timeUnit"]])


def reportTimeCompletion(evt):
    if evt["type"] == TimerEvent.COMPLETED:
        if timer.isTimer():
            playAlarm()


def reportMessages(evt):
    if evt["type"] == TimerEvent.WARNING:
        ui.message(f"{_('warning: ')} {evt['message']}")
    elif evt["type"] == TimerEvent.COMPLETED:
        if timer.isStopWatch():
            ui.message(getStatus())


def initializeTimer():
    global timer
    if not timer is None:
        return
    timer = Timer()
    timer.registerReporter(reportTimeCompletion)
    timer.registerReporter(reportMessages)
    if conf.getConfig("reportWithSound"):
        timer.registerReporter(reportWithSound)
    if conf.getConfig("reportWithSpeech"):
        timer.registerReporter(reportWithSpeech)


timePhases = {
    TimeUnit.SECONDS.name: 1,
    TimeUnit.MINUTES.name: 2,
    TimeUnit.HOURS: 3
}

initializeTimer()


def makeTime(currentTime, timeUnit):
    phases = timePhases[timeUnit.name]
    times = []
    cont = 0
    x = currentTime
    while cont < phases:
        x, r = divmod(x, 60)
        times.append("{0:0>2}".format(r))
        cont += 1

    times.reverse()
    formatedTime = ":".join(times)

    if int(times[0]) < 2:
        return f"{formatedTime} {getSingularTimeUnit(timeUnit)}"
    return f"{formatedTime} {timeUnit.name}"


def getStatus():
    if not timer.isRunning():
        status = _("stopped")
        if timer.isStopWatch() and timer.stopWatchResult is not None:
            status += f" {_('at')} {makeTime(timer.stopWatchResult, timer._timeUnit)}"
        return f"{timer._mode.value}: {status}"
    if timer.isTimer():
        return f"{timer._mode.value}: {makeTime(timer._counter, timer._timeUnit)} to finish{_(' (paused)') if timer.isPaused() else ''}"
    return f"{timer._mode.value}: {makeTime(timer._counter, timer._timeUnit)} elapsed{_(' (paused)') if timer.isPaused() else ''}"
