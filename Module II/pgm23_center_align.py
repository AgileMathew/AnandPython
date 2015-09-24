
'''Problem 23: Write a program center_align.py to center align all lines in the given file.'''

from sys import argv
lines=open(argv[1]).readlines()
length=0
for line in lines:
	if length<len(line):
		length=len(line)

for line in lines:
	print line.center(length)



