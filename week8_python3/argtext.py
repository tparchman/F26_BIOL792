#!/usr/bin/env python3

import sys

Infile = sys.argv[1]
Outfile= sys.argv[2]
print("Filename read in as argument: ", Infile,"\n","Filename provided for out: ", Outfile)
IN = open(sys.argv[1], 'r')

for Line in IN:
	Line=Line.strip("\n")
	print("The line of data is: ", Line)	
