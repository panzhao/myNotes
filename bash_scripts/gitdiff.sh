#!/bin/bash
#vimdiff "$2" "$5"
"/usr/bin/bcompare" "$2" "$5" | cat
#"/usr/local/bin/vimdiff" "$2" "$5" | cat
