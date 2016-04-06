#!/bin/sh
######################################################
#written by zhao pan <zhaopan@syberos.com>
#    该文件用于在所有的头文件中查找指定字符串
#
#
######################################################

if [ $# -eq 1 ];then
    SEARCH_PATH=.
    SEARCH_STR="$1"
elif [ $# -eq 2 ];then
    SEARCH_PATH=$1
    SEARCH_STR="$2"
else
    echo "[Usage] find_cpp [search_path] search_string"
    exit 0
fi

echo "find_h $SEARCH_PATH $SEARCH_STR"

find $SEARCH_PATH -name .git -prune -o -name "*.h" | xargs grep "$SEARCH_STR" -G -n --color=auto -i
