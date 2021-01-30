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
            self.warn(_("Initial time not configured. starting aborted"))
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
        log.debug(self._currentTime)
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


def secondsToTime(currentTime, targetTimeUnit, reduceTime=False):
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

    log.debug(str(resultUnits))
    # list is in order from seconds on. Revert it as to output time in readable order
    resultUnits.reverse()

    # remove trailing "00" if we are reducing time
    if reduceTime:
        while True:
            if resultUnits[0] != "00" or len(resultUnits) == 1:
                break
            resultUnits.pop(0)
        log.debug(str(resultUnits))
        # as we reduced time, the result time unit might have changed (e.e 00:01:30 hours now became 01:30 minuts)
        resultTimeUnit = timeUnits[len(resultUnits) - 1]

    formatedTime = ":".join(resultUnits)

    if int(resultUnits[0]) < 2:
        return f"{formatedTime} {getSingularTimeUnit(resultTimeUnit)}"
    return f"{formatedTime} {resultTimeUnit.value}"


def getStatus():
    # for stopwatch, time is always shown considering hours as time unit
    # for timer, we respect the timeUnit configured im timer object
    timeUnit = timer._timeUnit if timer.isTimer() else TimeUnit.HOURS
    # for stopwatch, we always reduce time
    # for timer, we respect the time format
    reduceTime = False if timer.isTimer() else True
    if not timer.isRunning():
        status = _("stopped")
        if timer.isStopWatch() and timer.stopWatchResult is not None:
            status += f" {_('at')} {secondsToTime(timer.stopWatchResult, timeUnit, reduceTime)}"
        return f"{timer._mode.value}: {status}"
    pausedStatus = _(" (paused)") if timer.isPaused() else ""
    ELAPSED = _("elapsed")
    TO_FINISH = _("to finish")
    if timer.isTimer():
        return f"{timer._mode.value}: {secondsToTime(timer._counter, timeUnit, reduceTime)} {TO_FINISH}{pausedStatus}"
    return f"{timer._mode.value}: {secondsToTime(timer._counter, timeUnit, reduceTime)} {ELAPSED}{pausedStatus}"
