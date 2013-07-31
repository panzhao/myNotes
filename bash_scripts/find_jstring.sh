#!/bin/bash
find ./ -name "*.java" | xargs grep $1 -n --color=auto
