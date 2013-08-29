#!/bin/sh 

# 指定vimdiff的路径. 
DIFF="/usr/bin/vimdiff" 

# svn提供第六和第七个参数作为base和本地最新的文本作为输入 
LEFT=${6} 
RIGHT=${7} 

#调用vimdiff做比较 
$DIFF $LEFT $RIGHT
