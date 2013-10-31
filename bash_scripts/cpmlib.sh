#/bin/bash
NFS_ANDROID_PATH=/home/zhaopan/nfs/android420
export SERVER_ANDROID_LIB_PATH=${NFS_ANDROID_PATH}/out/target/product/nusmart3_pad/system/lib
export SERVER_ANDROID_SYM_LIB_PATH=${NFS_ANDROID_PATH}/out/target/product/nusmart3_pad/symbols/system/lib

echo "cp lib  ... cp ${SERVER_ANDROID_LIB_PATH}/libnufront_webcore.so /home/zhaopan/webkit/webkit_420/trunk/BinFenTVBrowser/libs/armeabi"
cp ${SERVER_ANDROID_LIB_PATH}/libnufront_webcore.so /home/zhaopan/webkit/webkit_420/trunk/BinFenTVBrowser/libs/armeabi
echo "cp lib ok ..."
ls -l ${SERVER_ANDROID_LIB_PATH}/libnufront_webcore.so
ls -l /home/zhaopan/webkit/webkit_420/trunk/BinFenTVBrowser/libs/armeabi


echo "cp symbol lib ... cp ${SERVER_ANDROID_SYM_LIB_PATH}/libnufront_webcore.so /home/zhaopan/webkit_debug/external"
cp ${SERVER_ANDROID_SYM_LIB_PATH}/libnufront_webcore.so /home/zhaopan/webkit_debug/external
echo "cp symbol lib ok ..."
ls -l ${SERVER_ANDROID_SYM_LIB_PATH}/libnufront_webcore.so
ls -l /home/zhaopan/webkit_debug/external/libnufront_webcore.so
