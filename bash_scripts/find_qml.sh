#!/bin/sh
if [ $# -eq 1 ];then
    SEARCH_PATH=.
    SEARCH_STR="$1"
elif [ $# -eq 2 ];then
    SEARCH_PATH=$1
    SEARCH_STR="$2"
else
    echo "[Usage] find_qml [search_path] search_string"
    exit 0
fi

echo "find_qml.sh $SEARCH_PATH $SEARCH_STR"

find $SEARCH_PATH -name .git -prune -o \( -name "*.js" -o -name "*.qml" \) -print | xargs grep "$SEARCH_STR" -E -n --color=auto -i
