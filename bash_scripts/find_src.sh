#!/bin/sh
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

echo "find_src $SEARCH_PATH $SEARCH_STR"

#find $SEARCH_PATH -name .git -prune -o -name "*.cpp" -o -name "*.cc" -o -name "*.h" -o -name "*.cxx" -o -name "*.c" | xargs grep "$SEARCH_STR" -E -n --color=auto -i
find $SEARCH_PATH -name .git -prune -o  \( -name "*.cpp" -o -name "*.cc" -o -name "*.h"  -o -name "*.cxx"  -o -name "*.c" \) -print | xargs grep "$SEARCH_STR" -E -n --color=auto -i
 
