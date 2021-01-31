# Timer for NVDA 0.2.0-alpha
Brings timer and stopwatch functionalities right to NVDA

## download
Comming soon

## timers and stopwatches

A timer counts for a specified time down to 0. When it reaches 0, it completes and an alarm is emited.

A stopwatch starts counting from 0 and keeps running until instructed to stop. When this happens, it shows the elapsed time.

## Features

### sinple settings dialog

From a simple settings dialog, a timer or stop watch can be configured, as well as their progress monitoring options.

#### how it works

Press CTRL + NVDA + Shift + t to open the settings dialog.

* if either timer or stopwatch are running, you can:
    * Monitor progress by reading the settings dialog status bar.
    * Pause or stop the timer or stopwatch.
* if either timer or stopwatch are stopped, you can:
    * Configure the type of timer (timer or stopwatch)
    * adjust the time unit used (seconds, minutes or hours)
    * start the timer or the stopwatch.
* at any time, :you can
    * choose if progress is anounced with speech, beeps, both or none.

### run from NVDA commands

At any time, it is possible to start, stop, pause, resume and get status without having to use the settings dialog.

#### How it works

* press ctrl + shift + NVDA + s to start or stop timer or stopwatch.
    * If they are stopped, they will start, according to the last configuration made in the settings dialog.
    * if they are running, they will stop. Elapsed time is announced in case a stopwatch is running
    *     If there are not enough configuration to start a timer, a warning will be emited.
* press ctrl + shift + NVDA + p to pause or resume timer.
* press ctrl + shift + NVDA + r to hear timer or stopwatch progress. This is specially useful if all progress reporters are turned off and you want to check progress on demand.

### entering time

In the settings dialog, time is entered in hh:mm:ss format, where hh stands for hours, mm for minuts and ss for seconds.

It is not necessary to type the full format, the system will deduce it:

* if a simple number is entered, the selected time unit will be used.
* if sub units are specified, they will be considered: 01:05 becomes ome minut and five seconds, if selected time unit is minuts for example.
If the selected time unit is hours, 01:05 becomes one hour, five minuts and zero seconds.
* Sub units beyond seconds can not be specified. If time unit is minuts, 01:05:02 is not accepted.

### running timers and stopwatches

Only one timer or stopwatch can be started at a time.
Progress can be monitored using none, one or more reporters, by reading the timer dialog status bar or by issuing the report status command, ctrl+shift+nvda+r.
This way, it is perfectly possible to run the system with all reports turned off and monitor progress by reading the status bar when the dialog is open.

Commands to stop, start, pause, resume or get status report can be used even when the settings dialog is active.

There can be only one instance of the settings dialog running. If the settings dialog is closed, in progress executions of timer or stopwatch will keep running, and will be reflected if the dialog is opened again.

### time precision

Do not rely on extreme time precision when using this addon. This is due to the fact that python, the language NVDA is written in, can not execute more than one instruction at the same time, even if there are more than one processor or processor core available for use.

This means that every time NVDA speaks, calculates or processes anything, the time counting will have a slight delay.

The precision, however, should be good for the vast majority of cases, unless you need milisecond precision or otherwise will be severely impacted by any kind of delay.

For better precision results, reports should be turned off and status should be requested on demand either by issuing ctrl+sfift+nvda+r or by reading the status bar of the timer dialog.

### reporters

#### Sound reporter

When activated, this reporter plays a beep every time the timer or stopwatch counting reaches a round value, according to the time unit configured  in settings dialog.

For example, if the time unit configured is minuts, a beep is played every time counting reachs a full minut, which means it will beep every minut until the timer ends or the stopwatch is instructed to stop.

If you have configured a 02:30 minutes timer, a beep will be played when counting is at 02:00, and another one when it is at 01:00.

You can get the exact counting by reading the status bar of the settings dialog or by issuing the report status command, ctrl+shift+nvda+r.

### Speech reporter

When activated, this reporter says the current counting every time the timer or stopwatch counting reaches a round value, according to the time unit configured  in settings dialog.

For example, if the time unit configured is minuts, a counting status will be spoken every time counting reachs a full minut, which means it will report counting status every minut until the timer ends or the stopwatch is instructed to stop.

If you have configured a 02:30 minutes timer, "2" will be spoken when counting is at 02:00, and "1" will be spoken when it is at 01:00

You can get the exact counting by reading the status bar of the settings dialog or by issuing the report status command, ctrl+shift+nvda+r.

### timer end report

When a timer reaches 0, it has ended. This is signaled, independently of the settings dialog being active, with a discret alarm clock sound. This sound does not deppend on progress reporters, it will be played whenever a timer emds.

### stopwatch end report

When the stopwatch is instructed to stop, its elapsed time is spoken, independently of settings dialog being opened.

The elapsed time of the last stopwatch execution can be checked by reviewing the settings dialog status bar or pressing nvda+ctrl+shift+r. This information is reset when a new stopwatch or timer run starts.

# Contributing and translating

If you want to contribute or translate this addon, please access the [project repository](https://github.com/marlon-sousa/TimerForNVDA) and find instructions on the contributing.md in the english documentation directory
