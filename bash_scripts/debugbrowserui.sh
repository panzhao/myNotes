#!/bin/bash
pid=$(ps aux | awk '/\.\/CMOS_Browser/{print $2}');
echo $pid
gdb -x /home/zhaopan/myNotes/bash_scripts/gdbcfg --pid=$pid 
