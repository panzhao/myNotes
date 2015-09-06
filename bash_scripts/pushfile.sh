#!/bin/bash

echo $1

if [ -e $1 ]; then
    echo "$1 exists"
else
    echo "$1 not exists"
fi

scp $1  developer@192.168.100.100:/data/developer
