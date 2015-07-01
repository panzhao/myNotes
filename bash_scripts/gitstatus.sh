#!/bin/sh
if [ $# != 2];then
    echo $#
fi

STATUS=$1
OPRATE_MODE=$2


#git status | grep -E $STATUS | awk -F "[:]"  '{print $2}' | xargs $OPRATE_MODE
