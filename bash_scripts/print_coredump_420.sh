#!/bin/bash
ANDROID_PATH=`pwd`
SYM_PATH=out/target/product/nusmart3_pad/symbols/system/lib/
DIR_PATH=${ANDROID_PATH}/${SYM_PATH}
LIB_NAME=libnufront_webcore.so
FUNC_ADDRESS=
CMD_addr2line=${ANDROID_PATH}/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi-addr2line
if [[ $# -eq 2 ]]
then
LIB_NAME=$1
FUNC_ADDRESS=$2
elif [[ $# -eq 1 ]]
then
FUNC_ADDRESS=$1
elif [[ $# -eq 3 ]]
then
DIR_PATH=$1
LIB_NAME=$2
FUNC_ADDRESS=$3
else
  echo "[usage] $0 [lib_name] [func_address]"
  exit 0
fi
echo DIR_PATH=$DIR_PATH
echo LIB_NAME=$LIB_NAME
echo FUNC_ADDRESS=$FUNC_ADDRESS
${CMD_addr2line} -C -f -e ${DIR_PATH}/${LIB_NAME} ${FUNC_ADDRESS}
