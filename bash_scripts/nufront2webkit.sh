#!/bin/bash
if [[ $# -eq 1 ]];then
REPLACE_PROJECT="$1"
else
echo [Usage]: $0 "[c++|java]"
exit 1
fi
echo "REPLACE_PROJECT=$REPLACE_PROJECT"
if [ "$REPLACE_PROJECT" = "c++" ];then
echo replace c++
#for c++ project
find . -name "*.cpp" -o -name "*.cc" -o -name "*.c" -o -name "*.h" | xargs sed -i 's/com\/nufront/android/g'
find . -name "*.mk" | xargs sed -i 's/nufront_//g'
find . -name "*.cpp" -o -name "*.cc" -o -name "*.c" -o -name "*.h" | xargs sed -i 's/com\.nufrontcore/com\.android/g'
fi

#for java project : java file and xml file
if [ "$REPLACE_PROJECT" = "java" ];then
echo replace java
find . -name "*.java" -o -name "*.xml" | xargs sed -i 's/com\.nufrontcore/com\.android/g'
find . -name "*.java" | xargs sed -i 's/com\.nufront\.webkit/android\.webkit/g'
fi
