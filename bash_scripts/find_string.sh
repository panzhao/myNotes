#!/bin/bash
find ./ -name "*.cpp" -o -name "*.h" -o -name "*.c" -o -name "*.cc" -o -name "*.java" | xargs grep $1 -n --color=auto -i
