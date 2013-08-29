#!/bin/sh
if [ $# -eq 0 ];then
    SEARCH_PATH=.
elif [ $# -eq 1 ];then
    SEARCH_PATH=$1
else
    echo "[Usage] $0 [search_path]"
    exit 0
fi

ls -la ${SEARCH_PATH}/*.cpp
