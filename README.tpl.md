# Timer for NVDA ${addon_version}
Brings timer and stopwatch functionalities right to NVDA

## download
Comming soon

## Features

### sinple UI

From a simple dialog, you can configure your timer and stop watch and how you want to monitor progress.

#### how it works

Press CTRL + NVDA + Shift + T to open the timer dialog.

* if timer is running, you can:
    * Monitor progress by using regular NVDA statusbar reading command to read status bar.
    * Pause or stop the timer.
* if timer is stopped, you can:
    * Configure the type of timer (timer or stopwatch)
    * adjust the time unit used (seconds, minutes or hours)
    * start the timer.
* at any time, you can:
    * choose if progress is anounced with speech, beeps, both or none.

### run from NVDA keys

At any time, you can start, stop, pause, resume and get status without having to open the ui dialog.

#### How it works

Once you have started the timer, you can close the dialog and it will keep runing.

From outside of the dialog, you can:

* press ctrl + shift + NVDA + s to stop the timer.
    * If it is already stoped, it will start with the last configurations it had before.
    *     If it hasn't been ever started, a warning is emited.
* press ctrl + shift + NVDA + p to pause or resume timer.
* press ctrl + shift + nvda + r to hear timer progress. This is specially useful if all progress reporters are turned off and you want to check progress on demand.

### timer end report

When a timer reaches 0, it means that is has ended. This is signalized, independently of gui being opened, with a discret alarm clock sound. This sound does not deppend on progress reporters, it will be played whenever a timer emds.

# Contributing and translating

If you want to contribute or translate this addon, please access the [project repository](https://github.com/marlon-sousa/TimerForNVDA) and find instructions on the contributing.md in the english documentation directory
