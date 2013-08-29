#!/bin/bash
if [ $# -ne 1 ];then
    echo "[Usage] debug_nufront {1|2}"
    echo "        1 -- nufront"
    echo "        2 -- webkit"

    exit 0;
fi
SYMBOL_LIB_PATH=~/android/android4.0.3/out/target/product/generic/symbols/system/lib
#SYMBOL_LIB_PATH=~/android/IceCreamSandwich/out/target/product/generic/symbols/system/lib
WEBCORE_LIB=${SYMBOL_LIB_PATH}/libwebcore.so
WEBCORE_LIB_BAK="${WEBCORE_LIB}.bak"
NUFRONT_WEBCORE_LIB=${SYMBOL_LIB_PATH}/libnufront_webcore.so
NUFRONT_WEBCORE_LIB_BAK="${NUFRONT_WEBCORE_LIB}.bak"

echo $SYMBOL_LIB_PATH
echo $WEBCORE_LIB
echo $WEBCORE_LIB_BAK
echo $NUFRONT_WEBCORE_LIB
echo $NUFRONT_WEBCORE_LIB_BAK

echo "debug_nufront $1"
cd 
if [ $1 -eq 1 ];then
    if [ -f $NUFRONT_WEBCORE_LIB ] ;then
        echo "OK"
    else
        if [ -f $NUFRONT_WEBCORE_LIB_BAK ] ;then
            mv $NUFRONT_WEBCORE_LIB_BAK $NUFRONT_WEBCORE_LIB
        else
            echo "[Error] there is no $NUFRONT_WEBCORE_LIB and $NUFRONT_WEBCORE_LIB_BAK"
        fi
    fi 
    if [ -f $WEBCORE_LIB ];then
        mv $WEBCORE_LIB $WEBCORE_LIB_BAK
    fi
    ls -l $NUFRONT_WEBCORE_LIB
    ls -l $WEBCORE_LIB_BAK
elif [ $1 -eq 2 ];then
    if [ -f $WEBCORE_LIB ];then
        echo "OK"
    else
        if [ -f $WEBCORE_LIB_BAK ];then
            mv $WEBCORE_LIB_BAK $WEBCORE_LIB
        else
            echo "[Error] there is no $WEBCORE_LIB and $WEBCORE_LIB_BAK"
        fi
    fi
    if [ -f $NUFRONT_WEBCORE_LIB ];then
        mv $NUFRONT_WEBCORE_LIB $NUFRONT_WEBCORE_LIB_BAK
    fi
    ls -l $NUFRONT_WEBCORE_LIB_BAK
    ls -l $WEBCORE_LIB
else
    echo "[Usage] debug_nufront {1|2}"
    echo "        1 -- nufront"
    echo "        2 -- webkit"
fi
