#!/bin/sh
if [ $# -eq 2 ];then
    SEARCH_STR="$1"
    DEST_DIR="$2"
else
    echo "[Usage] please give [search_string] && destination"
    exit 0
fi

echo "search_str === $SEARCH_STR and dest_dir === $DEST_DIR" 
#files=`find . -name .git -prune -o -name .svn -o -name .repo -o -type f -iname  $SEARCH_STR`
files=`find .  -name .git -prune -o -name .svn -prune -o -name .repo -prune -o -type f -iname  $SEARCH_STR`

for arg in $files
do
    if [ -f $arg ];then
        echo $arg
        arg1=${arg##.}
        echo "cp $arg to $DEST_DIR$arg1"
        cp $arg $DEST_DIR$arg1
    fi
done
exit 0
