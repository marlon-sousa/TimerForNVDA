# Timer for NVDA 1.6.4
Brings timer and stopwatch functionalities right to NVDA

## download

Download the [ Simple Timer and stopwatch for NVDA 1.6.4 addon](https://github.com/marlon-sousa/TimerForNVDA/releases/download/1.6.4/TimerForNVDA-1.6.4.nvda-addon)

## timers and stopwatches

A timer counts for a specified time down to 0. When it reaches 0, it completes and an alarm is emited.

A stopwatch starts counting from 0 and keeps running until instructed to stop. When this happens, it shows the elapsed time.

## Features

### sinple settings dialog

A Timer or a stop watch can be configured from a simple settings dialog.

Different Progress monitoring reports  can also be configured from the same dialog.

#### how it works

Either use the "timer for NVDA settings" submenu  or press NVDA + Shift + t To open the addon settings dialog.
The submenu is located under NVDA "tools" menu.

* if either timer or stopwatch are running, you can:
    * Monitor progress by reading the settings dialog status bar.
    * Pause, resume or stop the timer or stopwatch.
* if either timer or stopwatch are stopped, you can:
    * Configure the operation mode (timer or stopwatch)
    * Configure  the time unit used for initial time value  for timer and also for reporting (seconds, minutes or hours)
    * start the timer or the stopwatch.
* at any time, you can:
    * choose if progress is anounced with speech, beeps, both or none.

### run from NVDA commands

At any time, it is possible to start, stop, pause, resume and get progress reports from a timer or stopwatch without having to use the settings dialog.

#### How it works

* press ctrl + shift + NVDA + s to start or stop timer or stopwatch.
    * If no timer or stopwatch is running, one of them will start, according to the current operation mode.
    * if one of them is running, it will stop. Elapsed time is announced in case a stopwatch was running
    *     In case a timer is starting and there are no previous initial time configured, a warning is emited.
* press ctrl + shift + NVDA + p to pause or resume a timer or stopwatch.
* press ctrl + shift + NVDA + r to check timer or stopwatch progress. This is specially useful if all progress reporters are turned off and you want to check progress on demand.

### entering time

In the settings dialog, initial time for timer is entered in HH:MM:SS format, where HH stands for hours, MM for minutes and SS for seconds.

It is not necessary to type the full format, the system will deduce it:

* if a simple number is entered, the selected time unit will be used.
* if sub units are specified, they will be considered. For example, 01:05 becomes one minute and five seconds, if selected time unit is "minutes".
If the selected time unit is "hours", 01:05 becomes one hour, five minutes and zero seconds.
* Sub units beyond "seconds" are invalid. If time unit is "minutes", the value 01:05:02 will not be accepted.

### running timers and stopwatches

Only one timer or stopwatch can be started at a time.
Progress can be monitored using none, one or more reporters, by reading the timer dialog status bar or by issuing the report status command, ctrl+shift+NVDA+r.
This way, it is perfectly possible to run the system with all reports turned off and monitor progress by reading the status bar when the dialog is opened.

Commands to stop, start, pause, resume or get on demand progress report can be used even when the settings dialog is active.

There can be only one instance of the settings dialog running. If the settings dialog is closed, in progress executions of timer or stopwatch will keep running.

If the settings dialog is opened while a timer or stopwatch is running, it will show updated information accordingly.

### time precision

This addon can not count time in an extremely precise way.

This happens because python, the language NVDA is written in, can not execute more than one instruction at the same time, even if there are more than one processor or processor core available for use.

Therefore, every time NVDA speaks, calculates or processes anything, the time counting will have a slight delay.

The precision, however, should be good for the vast majority of cases, unless milisecond precision is necessary or otherwise some process will be severely impacted by any kind of delay.

For better precision results, reports should be turned off and status should be requested on demand either by issuing ctrl+shift+NVDA+r or by reading the status bar of the timer dialog.

### reporters

#### Sound reporter

When activated, this reporter plays a beep every time the timer or stopwatch counting reaches a round value, according to the time unit configured  in settings dialog.

If you, for example, have configured a 02:30 minutes timer, a beep will be played when counting is at 02:00 minutes, and another one when it is at 01:00 minute.

You can get the exact counting by reading the status bar of the settings dialog or by issuing the report status command, ctrl+shift+NVDA+r.

#### Speech reporter

When activated, this reporter says the current time counting every time it reaches a round value, according to the time unit configured  in settings dialog.

If you, for example, have configured a 02:30 minutes timer, "2" will be spoken when counting is at 02:00 minutes, and "1" will be spoken when it is at 01:00 minute.

You can get the exact counting by reading the status bar of the settings dialog or by issuing the report status command, ctrl+shift+NVDA+r.

### timer completion report

When a time counting for a timer reaches 0, it has completed. This is signaled, independently of the settings dialog being active, with a discret alarm clock sound. This sound does not deppend on progress reporters being active.

### stopwatch completion report

When the stopwatch is stopped, its elapsed time is spoken, independently of the settings dialog being active.

The elapsed time of the last stopwatch execution can be checked by reviewing the settings dialog status bar or pressing NVDA+ctrl+shift+r. This information is reset when a new stopwatch or timer starts.

### Modify imput gestures

You can change default input gestures for this addon by accessing the "Timer for NVDA" section in the NVDA menu / Preferences / imput gestures dialog.

Remember that, should you change input gestures, you will need to choose options not used by other NVDA or external addon scripts in order to avoid conflicts.

# Contributing and translating

If you want to contribute or translate this addon, please access the [project repository](https://github.com/marlon-sousa/TimerForNVDA) and find instructions on the contributing.md in either your language or English language directory.

## Contributors

Special thanks to

* Marlon Brandão de Sousa - Brazilian Portuguese translation
* Tarik Hadžirović - Croatian translation
* Rémy Ruiz - French translation
* Ângelo Miguel Abrantes - Portuguese translation
* Rémy Ruiz - Spanish translation
* Umut KORKMAZ - Turkish translation
* Danil Kostenkov - Russian translation
* Heorhii - Ukrainian translation
* Brian Missao da Vera - NVDA 2022.1 compatibility
