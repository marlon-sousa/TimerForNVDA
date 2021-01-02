# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

from enum import auto, Enum, unique


@unique
class OperationMode(Enum):
    STOP_WATCH = _("Stopwatch")
    TIMER = _("Timer")


@unique
class TimeUnit(Enum):
    SECONDS = _("seconds")
    MINUTES = _("minutes")
    HOURS = _("hours")


@unique
class TimerEvent(Enum):
    STARTED = auto()
    STOPPED = auto()
    PAUSED = auto()
    RESUMED = auto()
    TICK = auto()
    COUNTER = auto()
    COMPLETED = auto()


@unique
class TimerStatus(Enum):
    STARTED = auto()
    STOPPED = auto()
    PAUSED = auto()


_units = {
    "SECONDS": 1,
    "MINUTES": 60,
    "HOURS": 3600
}

_singularTimeUnits = {
    "SECONDS": _("second"),
    "MINUTES": _("minute"),
    "HOURS": _("hour")
}


def getTime(timeUnit):
    return _units[timeUnit.name]


def getTimeUnits():
    return [i.value for i in TimeUnit]


def getOperationModes():
    return [i.value for i in OperationMode]


def getSingularTimeUnit(timeUnit):
    return _singularTimeUnits[timeUnit.name]
