#!/bin/bash
#cscope
find `pwd` -name "*.cpp" -o -name "*.h" -o -name "*.c" > cscope.files;
echo 'create cscope.out';
cscope -bqk -i cscope.files 
echo "cscope.files ok\n";

#ctags
echo "create ctasg"
ctags -R
echo "ctags ok";

#tags profile
echo "create curProFile.vim";
path=`pwd`;
string="set tags=`pwd`/tags";
echo "$string" > curProFile.vim;
echo "curProFile.vim ok \n";
