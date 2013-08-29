#!/bin/bash
find . -name efl | xargs rm -rf
find . -name qt | xargs rm -rf
find . -name wx | xargs rm -fr
find . -name wince | xargs rm -rf
find . -name gtk | xargs rm -rf
find . -name elf | xargs rm -rf
find . -name mac | xargs rm -rf
find . -name blackberry | xargs rm -rf
find . -name win | xargs rm -rf

