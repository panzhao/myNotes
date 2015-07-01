#!/bin/sh
if [ $# -eq 1 ];then
    SEARCH_PATH=.
    SEARCH_STR="$1"
elif [ $# -eq 2 ];then
    SEARCH_PATH=$1
    SEARCH_STR="$2"
else
    echo "[Usage] find_java [search_path] search_string"
    exit 0
fi

echo "find_java $SEARCH_PATH $SEARCH_STR"

find $SEARCH_PATH -name .git -prune -o -name "*.java" | xargs grep "$SEARCH_STR" -G -n --color=auto -i
