# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.


import config
import core
from logHandler import log
import threading
import time
import tones
from .types import getSingularTimeUnit, getTime, OperationMode, TimeUnit, TimerEvent, TimerStatus
import wx
import ui

timerRunning = False


class Timer:

    def __init__(self):
        self._resetState()
        self._running = False
        self._shouldRun = False
        self._thread = None
        self._mode = OperationMode.TIMER
        self._timeUnit = TimeUnit.SECONDS
        self._reporters = []
        self._counterLock = threading.Lock()

    def _resetState(self):
        self._currentTime = 0
        self._targetTime = 0
        self._status = TimerStatus.STOPPED

    def registerReporter(self, func):
        for f in self._reporters:
            if f == func:
                return
        self._reporters.append(func)

    def unregisterReport(self, func):
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

    def reportStatus(self, func):
        func(self._currentTime, self._targetTime, self._timeUnit, self._mode)

    def isTimer(self):
        return self._mode == OperationMode.TIMER

    def startTimer(self, initialTime, timeUnit):
        if self._shouldStart():
            self._status = TimerStatus.STARTED
            self._shouldRun = True
            self._thread = threading.Thread(
                target=self._timer, args=(initialTime,))
            self._thread.start()
            self._report(TimerEvent.STARTED)

    def pause(self):
        if self._thread is None:
            return
        self._shouldRun = False
        self._status = TimerStatus.PAUSED

    def stop(self):
        if self._thread is None:
            return
        self._shouldRun = False
        if self._thread != threading.current_thread() and self._thread.is_alive():
            self._thread.join()
        self._resetState()

    def _shouldStart(self):
        return self._thread is None or self._thread and not self._thread.is_alive()

    def _shouldStop(self):
        return not self._shouldRun

    def _incrementCurrentTime(self, counter):
        if counter % getTime(self._timeUnit) == 0:
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
                "status": self._status,
            })

    def _timer(self, initialTime):
        self._currentTime = initialTime
        self._targetTime = 0
        self._counter = initialTime * getTime(self._timeUnit)
        log.debug(str(self._counter))
        while self._counter > self._targetTime:
            log.debug("vamos esperar")
            time.sleep(1)
            log.debug("contandito")
            self._counter -= 1
            if self._counter % getTime(self._timeUnit) == 0:
                self._decrementCurrentTime()
                self._report(TimerEvent.TICK)
            if self._currentTime == 0 or self._shouldStop():
                break
        self.stop()
        self._report(TimerEvent.STOPPED)

    def _stopWatch(self):
        self.currentTime = 0
        self._counter = 0
        while True:
            time.sleep(1)
            self._counter += 1
            self.incrementCurrentTime()
            if self._shouldStop():
                break


beepDurations = {
    TimeUnit.SECONDS.value: 10,
    TimeUnit.MINUTES.value: 100,
    TimeUnit.HOURS.value: 200
}


def reportWithSpeech(evt):
    if evt["type"] == TimerEvent.TICK:
        ui.message(str(evt["currentTime"]))


def reportWithSound(evt):
    if evt["type"] == TimerEvent.TICK:
        tones.beep(4000, beepDurations[evt["timeUnit"]])


timer = Timer()


def makeTime(currentTime, timeUnit):
    if currentTime == 1:
        return f"1 {getSingularTimeUnit(timeUnit)}"
    return f"{currentTime} {timeUnit.name}"


def getStatus():
    if not timer.isRunning():
        return f"{timer._mode.name}: {_('stopped')}"
    if timer.isTimer():
        return f"{timer._mode.name}: {makeTime(timer._currentTime, timer._timeUnit)} to finish"
    return f"{timer._mode.name}: {makeTime(timer._currentTime, timer._timeUnit)} elapsed."
