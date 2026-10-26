#!/usr/bin/python

import re
import sys

print(sys.argv)
for file in sys.argv[1:]:
	sys.stderr.write("Processing file: %s \n" %(file))
	IN=open(file, 'r')
	OUT=open("out"+ file, 'w')
	sys.stderr.write("Opened file for writing: out%s \n" %(file))

	for Line in IN:
		Line=Line.strip("\n")
		OUT.write(Line + "\n")	
	IN.close()
	OUT.close()