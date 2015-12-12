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

find $SEARCH_PATH  \( -path "./.git" -o -name tags -o -name "cscope*" -o -name filenametags -o -name Session.vim -o -name curProFile.vim \) -prune -o -type f -print | xargs grep "$SEARCH_STR" -G -n  --color=auto -i -H

#find  /tmp/ \( -path "/tmp/123" -o -path "/tmp/234" -o -path "/tmp/345" \) -prune -o -type f -print

