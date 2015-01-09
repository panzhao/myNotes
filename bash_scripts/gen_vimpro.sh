#!/bin/bash
#cscope
if [ ! -f Session.vim ]; then
    echo "create new Session.vim ok"
    touch Session.vim
else 
    echo "has Session.vim, no need to create"
fi 

#find all source file
find `pwd` -name "*.cpp" -o -name "*.h" -o -name "*.c" > cscope.files;
cscope -bqk -i cscope.files 
echo "cscope.files ok";


#ctags
if [ ! -f tags ]; then
    echo "create new tags" 
else
    rm tags
    echo "rm old ctags ok";
fi    

#ctags -R --c++-kinds=+p --fields=+iaS --extra=+q

if [ ! -f .ycm_extra_conf.py ]; then
    echo "--------------------------"
    cp ~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py ./
else 
    echo ".ycm_extra_conf.py exist"
fi

#tags profile
#if [ ! -f curProFile.vim ]; then
#    path=`pwd`;
#    string="set tags+=`pwd`/tags";
#    string1="set path+=`pwd`/**/*"
#    echo "$string" > curProFile.vim;
#    echo "$string1" >> curProFile.vim;
#    echo "curProFile.vim ok";
#else
#   echo  "curProFile.vim exist, no need to create"
#fi

# 生成lookupfile索引文件
lookupfile.sh
