#!/bin/bash

######################################################
#written by zhao pan <zhaopan@syberos.com>
# 该脚本用于在上层目录生成MakeFile文件，并运行程序，命令行参数 
#
#
######################################################
appName=Desktop-nativeApp
srcdir=${PWD##*/}
echo $srcdir
BUILD_DIR=../build-$srcdir
echo $BUILD_DIR

echo ${USER}
sdk='/srv/syberos/sdks/sdk/syberos-sdk-chroot sb2 -t syberos-target-armv7tnhl'

if [ -d $BUILD_DIR ]; then
    echo "build-dir exisit"
else 
    mkdir $BUILD_DIR
fi

echo $BUILD_DIR/Makefile

if [ -e $BUILD_DIR/Makefile ]; then
    echo "Makefile exist"
else
    #echo ddddddddddddddddddddd
    cd $BUILD_DIR && $sdk qmake ../$srcdir
    cd ../$srcdir
fi

#echo pwd==========$PWD

echo zhaopan$BUILD_DIR
$sdk make -C $BUILD_DIR

#if [ $# == 1 ]; then
    #args=$1
    #echo minglinghangcanshu$args
    #./$BUILD_DIR/$appName $args
#else 
    #./$BUILD_DIR/$appName
#fi

pushfile.sh $BUILD_DIR/$appName
