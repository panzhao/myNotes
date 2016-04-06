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

echo "find_not_src $SEARCH_PATH $SEARCH_STR"

#find $SEARCH_PATH ! -name "*.cpp" -and ! -name "*.cc" -and ! -name "*.h" -and ! -name "*.cxx" -and ! -name "*.c" -and ! -name "*.svn" -and ! -name "*.git" -and ! -name "*tags" | xargs grep "$SEARCH_STR" -E -n --color=auto -i
find \( -name  "*.cpp" -o -name "*.cc" -o -name "*.c" -o -name "*.h" -o -name "*.cxx" -o -name ".svn" -o -name ".git" \) -prune  -o -print | xargs grep "$SEARCH_STR" -iEn --color=auto
