#!/bin/bash

######################################################
#written by zhao pan <zhaopan@syberos.com>
#       该文件主要用于本地rpm打包 
#       TODO: 使用sed自动获取Name和version
#
######################################################

#包名 一般工程目录即为包名参照:spec文件
#Name:		    page-manager
Name=page-manager    

#版本号,参照spec文件：
# Version:	0.0.1
Version=0.0.1

cd ..
echo $PWD
if [ -d $Name'-'$Version  ]; then
    echo "$Name'-'$Version exist"
    rm -rf $Name'-'$Version
else 
    echo "$Name'-'$Version not exist"
fi

#将当前目录修改为包名-版本号的格式, 参照spec文件：
#%setup -q -n %{name}-%{version}/%{name}, 该文件一半和工程目录相对应。
#               |         |         |
#               |         |         |
#             工程目录   版本号   源码目录    将本地工程按照以上代码构成复制，并打包。

path=$Name
cp -rf $path  $Name'-'$Version

#按照spec文件中压缩包的方式, 参照spec文件：
#Source0: %{name}-%{version}.tar.gz		
if [ -f  $Name'-'$Version.tar.gz ]; then
    echo "$Name'-'$Version.tar.gz exist"
    rm -rf $Name'-'$Version.tar.gz
else
    "$Name'-'$Version.tar.gz not exist"
fi

tar cvf  $Name'-'$Version.tar.gz $Name'-'$Version
 
cp $Name'-'$Version.tar.gz ~/rpmbuild/SOURCES/
spec=$Name/$Name.spec
cp $spec ~/rpmbuild/SPECS/

/srv/syberos/sdks/sdk/syberos-sdk-chroot sb2 -t syberos-target-armv7tnhl rpmbuild -ba ~/rpmbuild/SPECS/$Name.spec

#编译完成删除临时文件包
rm -rf $Name'-'$Version
rm -rf $Name'-'$Version.tar.gz $Name'-'$Version
scp /home/$USER/rpmbuild/RPMS/armv7tnhl/$Name'-'$Version'-'1.armv7tnhl.rpm developer@192.168.100.100:~

