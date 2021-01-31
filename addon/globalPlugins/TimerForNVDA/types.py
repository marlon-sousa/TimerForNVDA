# -*- coding: UTF-8 -*-
# A part of the TimerForNVDA addon for NVDA
# Copyright (C) 2021 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import addonHandler
from enum import auto, Enum, unique

addonHandler.initTranslation()


@unique
class OperationMode(Enum):
    # Translators: stopwatch
    STOP_WATCH = _("Stopwatch")
    # Translators: timer
    TIMER = _("Timer")


@unique
class TimeUnit(Enum):
    # Translators: seconds
    SECONDS = _("seconds")
    # Translators: minutes
    MINUTES = _("minutes")
    # Translators: hours
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
    WARNING = auto()
    ERROR = auto()


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
    # Translators: singular of seconds
    "SECONDS": _("second"),
    # Translators: singular of minutes
    "MINUTES": _("minute"),
    # Translators: singular of hours
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
