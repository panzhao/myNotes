#!/bin/bash
pid=$(adb shell ps|awk '/com.android.browser/{print $2}');
adb shell /system/bin/gdbserver :5039 --attach $pid;
