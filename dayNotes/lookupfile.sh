#!/bin/sh
# generate tag file for lookupfile plugin
echo -e "!_TAG_FILE_SORTED\t2\t/2=foldcase/" > filenametags
find . -not -regex '.*\.\(png\|gif\)' -type f -printf "%f\t%p\t1\n" | \
        sort -f >> filenametags 
#echo命令用来生成filenametags文件中的”!_TAG_FILE_SORTED”行，表明此tag文件是经过排序的。
#find命令用来查找所有类型为普通文件，文件后缀名不是.png和.gif的文件，找到的文件按”文件名\t文件路径\t1″的格式输出出来。
#sort命令则把find命令的输出重新排序，然后写入filenametags文件中
