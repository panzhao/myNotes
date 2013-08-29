#/bin/bash
ANDROID_PATH=~/android/google_android403r1/google_android403r1/
ANDROID_IMG_PATH=${ANDROID_PATH}/out/target/product/generic
emulator -system ${ANDROID_IMG_PATH}/system.img -data ${ANDROID_IMG_PATH}/userdata.img -ramdisk ${ANDROID_IMG_PATH}/ramdisk.img -partition-size 500 -sdcard ${ANDROID_IMG_PATH}/sdcard.img&
