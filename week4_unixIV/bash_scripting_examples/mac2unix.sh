#!/bin/zsh

cat $1 | tr '\r' '\n' > unix_$1