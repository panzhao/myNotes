#!/bin/bash

######################################################
#written by zhao pan <zhaopan@syberos.com>
# 该脚本用于在上层目录生成MakeFile文件，并运行程序，命令行参数 
#
#
######################################################
#appName=Desktop-nativeApp
srcdir=${PWD##*/}
echo $srcdir
BUILD_DIR=../build-$srcdir
echo $BUILD_DIR

echo ${USER}
sdk='/srv/syberos/sdks/sdk/syberos-sdk-chroot sb2 -t syberos-target-armv7tnhl'

if [ -d $BUILD_DIR ]; then
    echo -e "\033[32m $BUILD_DIR  exists \033[0m"
else 
    echo -e "\033[31m $BUILD_DIR  not exists,should create it. \033[0m"
    mkdir $BUILD_DIR
    if [ -d $BUILD_DIR ]; then
        echo -e "\033[32m $BUILD_DIR create sucess. \033[0m"
    fi
fi


echo $BUILD_DIR/Makefile

if [ -e $BUILD_DIR/Makefile ]; then
    echo -e "\033[32m Makefile exist \033[0m"
else
    #echo ddddddddddddddddddddd
    echo -e "\033[32m Makefile not exist, we create \033[0m"
    cd $BUILD_DIR && $sdk qmake ../$srcdir
    cd ../$srcdir
fi

#echo pwd==========$PWD

echo zhaopan$BUILD_DIR
$sdk make -j8 -C $BUILD_DIR

if [ $? != 0 ]; then
    echo -e "\033[31m compile error \033[0m"
    exit -1;
fi

#if [ $# == 1 ]; then
    #args=$1
    #echo minglinghangcanshu$args
    #./$BUILD_DIR/$appName $args
#else 
    #./$BUILD_DIR/$appName
#fi

push2yuanxinos.sh $BUILD_DIR/test/testPageManager
find $BUILD_DIR  -name "*.so*" -exec push2yuanxinos.sh {} \;
