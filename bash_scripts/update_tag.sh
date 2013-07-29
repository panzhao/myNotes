#!/bin/bash

ctags -R
cscope -Rbqk

vim
echo "成功生成tags"
