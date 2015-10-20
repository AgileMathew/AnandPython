"""Problem 2: Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension."""


import sys
import os

fn=sys.argv[1]
def extcount(fn):
	count = 0
	xs=os.listdir(fn)
	l = []
	for i in xs:
		d=i.split('.')
		l.append(d[1])
#def word_frequency(words):
	frequency = {}
	for w in l:
		frequency[w]=frequency.get(w,0)+1
	
	for key,value in frequency.items():

		print value,key
extcount(fn)
