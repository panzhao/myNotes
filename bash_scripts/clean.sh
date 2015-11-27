#!/bin/bash

srcdir=${PWD##*/}
BUILD_DIR=../build-$srcdir

make distclean -C $BUILD_DIR
