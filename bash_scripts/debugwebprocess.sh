#!/bin/bash
pid=$(ps aux | awk '/QtWebProcess/{print $2}');
echo $pid
gdb -x /home/zhaopan/myNotes/bash_scripts/gdbcfg --pid=$pid 
