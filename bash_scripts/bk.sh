#!/bin/sh
dir=${PWD##*/}
time=`date +%y.%m.%d'_'%H.%M.%S`
user=`hostname`
tar --exclude='*.pro.user*' --exclude='build-*' --exclude='.*' --exclude-vcs -acf ../$dir.$time.$user.tar.xz *
