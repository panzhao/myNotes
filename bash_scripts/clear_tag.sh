#!/bin/sh

rm cscope.*
rm .ycm_extra_conf.pyc
rm .ycm_extra_conf.py
rm tags
rm curProFile.vim
rm filenametags
rm Session.vim
rm clean.sh
if [ -e "run.sh" ]; then
    rm run.sh
fi
if [ -e "clean.sh" ]; then
    rm clean.sh
fi
