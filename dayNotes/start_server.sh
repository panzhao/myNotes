#!/bin/bash
pid=$(adb shell ps|awk '/com.binfen.tvbrowser/{print $2}');
adb shell /system/bin/gdbserver :5039 --attach $pid;
