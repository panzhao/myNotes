#!/bin/sh
if [ $# -eq 1 ];then
    SEARCH_PATH=`pwd`
    SEARCH_FILE="$1"
elif [ $# -eq 2 ];then
    SEARCH_PATH=$1
    SEARCH_FILE="$2"
else
    echo "[Usage] find_cpp [search_path] search_string"
    exit 0
fi

#echo "$0 $SEARCH_PATH $SEARCH_FILE"

find $SEARCH_PATH -name "${SEARCH_FILE}"
