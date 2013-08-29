#/bin/bash
export ANDROID_PATH=/home/bdg/android/google_android403r1/google_android403r1
if [[ -f $1 ]]
then
    cp $1 ${ANDROID_PATH}/out/target/product/generic/
fi
if [[ -f $2 ]]
then
    cp $2 ${ANDROID_PATH}/out/target/product/generic/
fi
if [[ -f $3 ]]
then
    cp $3 ${ANDROID_PATH}/out/target/product/generic/
fi
