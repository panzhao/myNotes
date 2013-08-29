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
find . -name "*.cpp" -o -name "*.cc" -o -name "*.c" -o -name "*.h" | xargs sed -i 's/android\/webkit/com\/nufront\/webkit/g'
find . -name "*.cpp" -o -name "*.cc" -o -name "*.c" -o -name "*.h" | xargs sed -i 's/com\.android/com\.nufrontcore/g'

# mk
find . -name "*.mk" | xargs sed -i 's/libwebcore/libnufront_webcore/g'
find . -name "*.mk" | xargs sed -i 's/libchromium_net/libnufront_chromium_net/g'
find . -name "*.mk" | xargs sed -i 's/libv8/libnufront_v8/g'

# mk 文件需要手工合并


# v8

# chromium
fi






#for java project : java file and xml file
if [ "$REPLACE_PROJECT" = "java" ];then
echo replace java
1. 
find . -name "*.java" -o -name "*.xml" | xargs sed -i 's/android\.webkit/com\.nufront\.webkit/g'
find . -name "*.java" -o -name "*.xml" | xargs sed -i 's/com\.android\.browser/com\.nufrontcore\.browser/g'

2. 
cp ~/tmp/bouncycastle/ src/com/nufrontcore/browser/ -ra
find . -name "*.java" -o -name "*.xml" | xargs sed -i 's/com\.android\.org\.bouncycastle/com\.nufrontcore\.browser\.bouncycastle/g'
find . -name "*.java" -o -name "*.xml" | xargs sed -i 's/org\.bouncycastle/com\.nufrontcore\.browser\.bouncycastle/g'


3. 
cp util/ src/com/nufrontcore/browser/ -ra 
(EventLogTags.java)

find . -name "*.java" -o -name "*.xml" | xargs sed -i 's/android\.util/com\.nufrontcore\.browser\.util/g'


4. 
cp libcore/luni/src/main/java/libcore/net/MimeUtils.java ./src/com/nufront/webkit/

cp ./libcore/luni/src/main/java/org/apache/harmony/xnet/provider/jsse/NativeCrypto.java 

com.android.org.bouncycastle

fi
