#/bin/bash
export RSA_PUB_PATH=/home/bdg/bak/client.bak/ssh_rsa
export CLIENT_64_RSA_PUB_FILE=id_rsa.pub.64
export CLIENT_32_RSA_PUB_FILE=id_rsa.pub.32
if [ $# -eq 1 ];then
if [ $1 -eq "32" ];then
    if [ -f ${RSA_PUB_PATH}/${CLIENT_32_RSA_PUB_FILE} ];then
        echo "[Warning] using ssh rsa file [${RSA_PUB_PATH}/${CLIENT_32_RSA_PUB_FILE}]"
        ssh-keygen -f "/home/bdg/.ssh/known_hosts" -R 192.168.16.136
        cat  ${RSA_PUB_PATH}/${CLIENT_32_RSA_PUB_FILE} > ~/.ssh/authorized_keys
    else
        echo "[Error] rsa pub file is not exist! [${RSA_PUB_PATH}/${CLIENT_32_RSA_PUB_FILE}]"
    fi
elif [ $1 -eq "64" ];then
    if [ -f ${RSA_PUB_PATH}/${CLIENT_64_RSA_PUB_FILE} ];then
        echo "[Warning] using ssh rsa file [${RSA_PUB_PATH}/${CLIENT_64_RSA_PUB_FILE}]"
        ssh-keygen -f "/home/bdg/.ssh/known_hosts" -R 192.168.16.136
        cat  ${RSA_PUB_PATH}/${CLIENT_64_RSA_PUB_FILE} > ~/.ssh/authorized_keys
    else
        echo "[Error] rsa pub file is not exist! [${RSA_PUB_PATH}/${CLIENT_64_RSA_PUB_FILE}]"
    fi
else
    echo "[Usage] $0 [32|64]"
    exit 0
fi
else
    echo "[Usage] $0 [32|64]"
    exit 0
fi
