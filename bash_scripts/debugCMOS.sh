#!/bin/bash
pid=$(ps aux | awk '/\.\/CMOS_Browser/{print $2}');
gdb --pid=$pid
