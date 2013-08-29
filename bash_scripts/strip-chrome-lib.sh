#!/bin/bash
# strip libchromeview.so and scp to client
ANDROID_404_PATH=/home/bdg/android4.0.4/android-404
ANDROID_STRIP_PATH=${ANDROID_404_PATH}/prebuilt/linux-x86/toolchain/arm-eabi-4.4.3/bin/arm-eabi-strip
CHROMEVIEW_LIB_PATH=${ANDROID_404_PATH}/external/chrome/out/Release/lib.target/libchromeview.so
CHROME_APK_PATH=${ANDROID_404_PATH}/external/chrome/apk
CHROME_TMP_APK_PATH=${CHROME_APK_PATH}/Chrome/
CHROME_TMP_APK_NAME=Chrome.apk
echo "1) stripping libchromeview.so ..."
if [ ! -f ${ANDROID_STRIP_PATH} ];then
  echo "[Error] arm-eabi-strip not exist[${ANDROID_STRIP_PATH}]!"
  exit
fi
if [ ! -f ${CHROMEVIEW_LIB_PATH} ];then
  echo "[Error] libchromeview.so not exist![${CHROMEVIEW_LIB_PATH}]"
  exit
fi
${ANDROID_STRIP_PATH} ${CHROMEVIEW_LIB_PATH}
ls -lt  ${ANDROID_404_PATH}/external/chrome/out/Release/lib.target/libchromeview.so

echo "2) scp to client : libchromeview.so"
scp_single.sh ${ANDROID_404_PATH}/external/chrome/out/Release/lib.target/libchromeview.so
