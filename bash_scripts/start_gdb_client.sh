#!/bin/bash
adb forward tcp:5039 tcp:5039
 /home/zhaopan/android/master/prebuilts/gcc/linux-x86/arm/arm-eabi-4.8/bin/arm-eabi-gdb -x /home/zhaopan/myNotes/bash_scripts/gdbcfg  /home/zhaopan/android/master/out/target/product/generic/symbols/system/bin/app_process
target remote:5039
