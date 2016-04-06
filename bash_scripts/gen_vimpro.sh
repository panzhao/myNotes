#!/bin/bash
#cscope
if [ ! -f Session.vim ]; then
    echo 
    echo -e "\033[32m create new Session.vim ok\033[0m"
    touch Session.vim
else 
    rm Session.vim
    touch Session.vim
    echo -e "\033[31mSession.vim exists, recreate it\033[0m"
fi 

#find all source file
find `pwd` -name "*.cpp" -o -name "*.h" -o -name "*.c" -o -name "*.java" > cscope.files;
#cscope -bqk -i cscope.files 
echo "cscope.files ok";


#ctags
if [ ! -f tags ]; then
    echo "create new tags" 
else
    rm tags
    echo "rm old ctags ok";
fi    

ctags -R --c++-kinds=+p --fields=+iaS --extra=+q

if [ ! -f .ycm_extra_conf.py ]; then
    echo ".ycm_extra_conf.py not exist"
    cp /home/zhaopan/myNotes/bash_scripts/ycm_extra_conf.py ./.ycm_extra_conf.py
else
    echo ".ycm_extra_conf.py exist"
fi

#tags profile
if [ ! -f curProFile.vim ]; then
    path=`pwd`;
    string="set tags+=`pwd`/tags";
    string1="set path+=`pwd`/**/*"
    string2='"autocmd FileType c,cpp,h map<silent><leader><F5> :w <CR> :make <CR> :cw <CR> :cc <cr>'
    string3='"map<silent><leader><F6> :w <CR> :! ./run.sh <cr>'
    string4='map<silent><leader><F7> :w <CR> :! clean.sh <cr>'
    gen_vim='map<silent><leader><F4> :! gen_vimpro.sh <cr>'

    echo "$string" >> curProFile.vim;
    echo "$string1" >> curProFile.vim;
    echo "$string2" >> curProFile.vim;
    echo "$string3" >> curProFile.vim;
    echo "$string4" >> curProFile.vim;
    echo "$gen_vim" >> curProFile.vim;
    echo "curProFile.vim ok";
else
   echo  "curProFile.vim exist, no need to create"
fi
if [ -e run.sh ]; then
    echo "run.sh exists."
else
    cp /home/$USER/myNotes/bash_scripts/run.sh   ./
fi
#cp /home/zhaopan/myNotes/bash_scripts/clean.sh ./
# 生成lookupfile索引文件
lookupfile.sh
