#!/bin/bash
if [ $# -ne 1 ];then
echo "[Usage] $0 <version-svn>"
exit 1
fi

echo "sync ..."
ls aaaaaaaaa
while [ $? -ne 0 ]
do
    echo "sync ..."
    svn up -r $1 >> svn.up.$1.log
done
