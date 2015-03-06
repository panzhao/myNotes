#!/bin/sh
if [ $# -eq 1 ];then
    SEARCH_PATH=.
    SEARCH_STR="$1"
elif [ $# -eq 2 ];then
    SEARCH_PATH=$1
    SEARCH_STR="$2"
else
    echo "[Usage] find_all [search_path] search_string"
    exit 0
fi

echo "find_all $SEARCH_PATH $SEARCH_STR"

find $SEARCH_PATH ! -name "*.svn*" -o ! -name "*tags" | xargs grep "$SEARCH_STR" -G -n --color=auto -i
