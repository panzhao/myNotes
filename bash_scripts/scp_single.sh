#/bin/sh
echo copying $1 ...
TARGET_IP=192.168.16.136
if [[ -d $1 ]]
then
    scp -r $1 bdg@${TARGET_IP}:/home/bdg/tmp
elif [[ -f $1 ]]
then
    scp $1 bdg@${TARGET_IP}:/home/bdg/tmp
fi
if [[ -d $2 ]]
then
    scp -r $2 bdg@${TARGET_IP}:/home/bdg/tmp
elif [[ -f $2 ]]
then
    scp $2 bdg@${TARGET_IP}:/home/bdg/tmp
fi
if [[ -d $3 ]]
then
    scp -r $3 bdg@${TARGET_IP}:/home/bdg/tmp
elif [[ -f $3 ]]
then
    scp $3 bdg@${TARGET_IP}:/home/bdg/tmp
fi
