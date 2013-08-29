#/bin/bash
export SERVER_ANDROID_LIB_PATH=${NFS_ANDROID_PATH}/out/target/product/generic/system/lib
export SERVER_ANDROID_SYM_PATH=${NFS_ANDROID_PATH}/out/target/product/generic/symbols/system/lib

echo "cp lib  ... cp ${SERVER_ANDROID_LIB_PATH}/libnufront_webcore.so ${WORKSPACE_PATH}/BrowserActivity/libs/armeabi/"
cp ${SERVER_ANDROID_LIB_PATH}/libnufront_webcore.so ${WORKSPACE_PATH}/BrowserActivity/libs/armeabi/
echo "cp lib ok ..."
ls -l ${SERVER_ANDROID_LIB_PATH}/libnufront_webcore.so
ls -l ${WORKSPACE_PATH}/BrowserActivity/libs/armeabi/libnufront_webcore.so


echo "cp symbol lib ... cp ${SERVER_ANDROID_SYM_PATH}/libnufront_webcore.so ${ANDROID_PATH}/out/target/product/generic/symbols/system/lib"
cp ${SERVER_ANDROID_SYM_PATH}/libnufront_webcore.so ${ANDROID_PATH}/out/target/product/generic/symbols/system/lib
echo "cp symbol lib ok ..."
ls -l ${SERVER_ANDROID_SYM_PATH}/libnufront_webcore.so
ls -l ${ANDROID_PATH}/out/target/product/generic/symbols/system/lib/libnufront_webcore.so
