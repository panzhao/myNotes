#!/bin/sh
if [ $# != 2];then
    echo $#
fi

STATUS=$1
OPRATE_MODE=$2


git status | grep -E "(modified:|new file:)" | awk -F "[:]"  '{print $2}' | xargs git add
