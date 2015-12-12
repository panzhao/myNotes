#!/bin/bash

echo $1

if [ -e $1 ]; then
    echo -e "\033[32m $1 exists \033[0m"
else
    echo -e "\033[31m $1 not existes \033[0m"
fi

#scp -r $1  developer@192.168.100.100:/data/developer

cdb push  $1 /data/developer
