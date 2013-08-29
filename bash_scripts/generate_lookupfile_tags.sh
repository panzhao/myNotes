#!/bin/sh
# generate tag file for lookupfile plugin
echo "!_TAG_FILE_SORTED\t2\t/2=foldcase/" > filenametags
find . -regex '.*\.\(cpp\|h\|c\|cc\|java\)' -type f -printf "%f\t%p\t1\n" | sort -f >> filenametags 
#find . -not -regex '.*\.\(cpp\|h\)' -type f -printf "%f\t%p\t1\n" | sort -f >> filenametags 
