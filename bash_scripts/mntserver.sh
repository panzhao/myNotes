#/bin/bash
# mount server to local
sudo mount -t nfs -o nfsvers=3,timeo=3,udp 192.168.19.122:/home/bdg/ ~/mnt/
