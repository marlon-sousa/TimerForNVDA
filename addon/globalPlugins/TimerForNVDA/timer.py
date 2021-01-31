# -*- coding: UTF-8 -*-
# A part of the TimerForNVDA addon for NVDA
# Copyright (C) 2021 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import addonHandler
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

addonHandler.initTranslation()

# Translators: timer
TIMER = _("timer")
# Translators: stop watch
STOP_WATCH = _("stopwatch")

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

    def _resetState(self):
        self._currentTime = "0"
        self._targetTime = 0
        self._status = TimerStatus.STOPPED
        self._message = ""
        self._counter = 0

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
            self._currentTime = "0"
            self._run()
            self._report(TimerEvent.STARTED)

    def start(self, initialTime=None):
        if self.isTimer():
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
            # Translators: can not pause
            CAN_NOT_PAUSE = _("Can not pause")
            # Translators: because it is not running
            BECAUSE_IT_IS_NOT_RUNNING = _("because it is not running")
            self.warn(
                f"{CAN_NOT_PAUSE} {TIMER if self.isTimer() else STOP_WATCH} {BECAUSE_IT_IS_NOT_RUNNING}")
            return
        self._shouldRun = False
        if self._thread != threading.current_thread() and self._thread.is_alive():
            self._thread.join()
        self._status = TimerStatus.PAUSED
        self._report(TimerEvent.PAUSED)

    def resume(self):
        if not self.isPaused():
            # Translators: can not pause
            CAN_NOT_RESUME = _("Can not resume")
            # Translators: because it is not running
            BECAUSE_IT_IS_NOT_PAUSED = _("because it is not paused")
            self.warn(
                f"{CAN_NOT_RESUME} {TIMER if self.isTimer() else STOP_WATCH} {BECAUSE_IT_IS_NOT_PAUSED}")
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
        if self._shouldRun:
            return
        self._shouldRun = True
        self._thread = threading.Thread(
            target=(self._timer if self.isTimer() else self._stopWatch))
        self._thread.start()

    def warn(self, warning):
        self._message = warning
        self._report(TimerEvent.WARNING)

    def _shouldStart(self, initialTime=None):
        if self.isTimer() and not initialTime and not self._initialTime:
            # Translators: initial time not configured. Start aborted
            self.warn(_("Initial time not configured. start aborted"))
            return False
        return self._thread is None or self._thread and not self._thread.is_alive()

    def _shouldStop(self):
        return not self._shouldRun

    # normalize time to complete descriptor, according to current time unit
    # for example, if we send "01" (simple value), we will have "00:01:00"
    # in case current time unit is minuts, or "01:00:00" in case the current time unit is hours
    # if current time iunit is seconds, we will have "00:00:01"
    def _normalizeTime(self):
        timeUnits = self._currentTime.split(":")
        expectedAmountUnits = timePhases[self._timeUnit.name] + 1
        if len(timeUnits) > expectedAmountUnits:
            # Translators: could not normalize time
            self._status = _("Could not mormalize time")
            self._report(TimerEvent.ERROR)
            raise Exception(self._status)
        # filling sub units with "00"
        while len(timeUnits) < expectedAmountUnits:
            timeUnits.append("00")
        # filling super units
        while len(timeUnits) <= timePhases[TimeUnit.HOURS.name]:
            timeUnits.insert(0, "00")
        self._currentTime = ":".join(timeUnits)

    def _isTick(self):
        return self._counter % getTime(self._timeUnit) == 0

    def _currentTimeToSeconds(self):
        self._normalizeTime()
        timeUnits = (self._currentTime.split(":"))
        if len(timeUnits) > 3:
            raise Exception("Invalid time error")
        conversionFactors = [3600, 60, 1]
        result = 0
        for unit in range(len(timeUnits)):
            result = result + (int(timeUnits[unit]) * conversionFactors[unit])
        return result

    def _initializeCounter(self):
        # if counter has vvalue, process is likely resuming. Use current value
        if not self._counter:
            # convert time format of initial time to seconds
            self._counter = self._currentTimeToSeconds()

    def _report(self, evt):
        for reporter in self._reporters:
            wx.CallAfter(reporter, {
                "type": evt,
                "currentTime": self._currentTime,
                "counter": self._counter,
                "timeUnit": self._timeUnit.value,
                "watchType": self._mode.value,
                "message": self._message,
                "status": self._status,
            })

    def _timer(self):
        self._targetTime = 0
        self._initializeCounter()
        while self._counter > self._targetTime:
            if self._shouldStop():
                break
            time.sleep(1)
            self._counter -= 1
            self._report(TimerEvent.COUNTER)
            if self._isTick():
                self._currentTime = secondsToTime(
                    self._counter, self._timeUnit, formatTime=False)
                self._report(TimerEvent.TICK)
            if self._counter == 0:
                self._report(TimerEvent.COMPLETED)
                self.stop()
                break

    def _stopWatch(self):
        self._initializeCounter()
        while True:
            if self._shouldStop():
                break
            time.sleep(1)
            self._counter += 1
            self._report(TimerEvent.COUNTER)
            if self._isTick():
                self._currentTime = secondsToTime(
                    self._counter, self._timeUnit, formatTime=False)
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
    if evt["type"] == TimerEvent.TICK and evt["counter"] != 0:
        ui.message(str(evt["currentTime"]))


def reportWithSound(evt):
    if evt["type"] == TimerEvent.TICK and evt["counter"] != 0:
        tones.beep(4000, beepDurations[evt["timeUnit"]])


def reportTimeCompletion(evt):
    if evt["type"] == TimerEvent.COMPLETED:
        if timer.isTimer():
            playAlarm()


def reportMessages(evt):
    if evt["type"] == TimerEvent.WARNING:
        # Translators: warning
        ui.message(f"{_('warning: ')} {evt['message']}")
    elif evt["type"] == TimerEvent.COMPLETED:
        if timer.isStopWatch():
            ui.message(getStatus())


def initializeTimer():
    global timer
    if timer is not None:
        return
    timer = Timer()
    timer.registerReporter(reportTimeCompletion)
    timer.registerReporter(reportMessages)
    if conf.getConfig("reportWithSound"):
        timer.registerReporter(reportWithSound)
    if conf.getConfig("reportWithSpeech"):
        timer.registerReporter(reportWithSpeech)


timePhases = {
    TimeUnit.SECONDS.name: 0,
    TimeUnit.MINUTES.name: 1,
    TimeUnit.HOURS.name: 2
}

initializeTimer()


def getReducedTime(units):
    timeUnits = list(TimeUnit)
    # remove trailing "00"
    while True:
        if units[0] != "00" or len(units) == 1:
            break
        units.pop(0)

    # as we reduced time, the time unit needs to be recalculated (e.e 00:01:30 hours now became 01:30 minuts)
    timeUnit = timeUnits[len(units) - 1]

    # if sub units are zeroed, we also need to remove them
    while True:
        if units[-1] != "00" or len(units) == 1:
            break
        units.pop()

    units[0] = units[0].lstrip("0")
    return (units, timeUnit)


def secondsToTime(currentTime, targetTimeUnit, reduceTime=True, formatTime=True):
    resultUnits = []
    resultTimeUnit = targetTimeUnit
    timeUnits = list(TimeUnit)
    currentUnit = currentTime
    # because currentUnit, at this time, is always in seconds, we process it and its sub units untill we reach the target time unit
    for timeUnit in timeUnits:
        if timeUnit == targetTimeUnit:
            # target unit won't be converted
            resultUnits.append("{0:0>2}".format(currentUnit))
            break
        # convert unit. It should be no greater than 59 and the difference is considered the next time unit
        nextUnit, currentUnit = divmod(currentUnit, 60)
        resultUnits.append("{0:0>2}".format(currentUnit))
        currentUnit = nextUnit

    # list is in order from seconds on. Revert it as to output time in readable order
    resultUnits.reverse()

    if reduceTime:
        resultUnits, resultTimeUnit = getReducedTime(resultUnits)

    result = ":".join(resultUnits)

    if formatTime:
        result = f"{result} {getSingularTimeUnit(resultTimeUnit) if int(resultUnits[0]) < 2 else resultTimeUnit.value}"
    return result


def getStatus():
    # for stopwatch, time is always shown considering hours as time unit
    # for timer, we respect the timeUnit configured im timer object
    timeUnit = timer._timeUnit if timer.isTimer() else TimeUnit.HOURS

    if not timer.isRunning():
        # Translators: stopped
        status = _("stopped")
        if timer.isStopWatch() and timer.stopWatchResult is not None:
            # Translators: preposition after word stopped for stopwatch
            status += f" {_('at')} {secondsToTime(timer.stopWatchResult, timeUnit)}"
        return f"{timer._mode.value}: {status}"
    # Translators: paused
    pausedStatus = _(" (paused)") if timer.isPaused() else ""
    # translators: elapsed
    ELAPSED = _("elapsed")
    # Translators: to finish
    TO_FINISH = _("to finish")
    if timer.isTimer():
        return f"{timer._mode.value}: {secondsToTime(timer._counter, timeUnit)} {TO_FINISH}{pausedStatus}"
    return f"{timer._mode.value}: {secondsToTime(timer._counter, timeUnit)} {ELAPSED}{pausedStatus}"
