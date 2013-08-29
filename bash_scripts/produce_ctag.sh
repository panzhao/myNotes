#!/bin/bash
echo "generating... ctags"
if [[ -f "tags" ]]
then
  rm tags -f
fi
ctags -R

# generate cscope
echo "generating... cscope file"
if [[ -f "cscope.files" || -f "cscope.out" ]]
then
  rm cscope* -f
fi
find . -name "*.cpp" -o -name "*.cc" -o -name "*.cxx" -o -name "*.c" -o -name "*.h" -o -name "*.java" > cscope.files 
echo "generating... cscope tag"
cscope -bkR

# generate lookupfile tag
echo "generating... lookupfile tag"
if [[ -f "filenametags" ]]
then
  rm filenametags -f
fi
echo "!_TAG_FILE_SORTED\t2\t/2=foldcase/" > filenametags
find . -regex '.*\.\(cpp\|h\|c\|cc\|java\)' -type f -printf "%f\t%p\t1\n" | sort -f >> filenametags
#find . -not -regex '.*\.\(cpp\|h\)' -type f -printf "%f\t%p\t1\n" | sort -f >> filenametags 

echo "---generating ok---"
