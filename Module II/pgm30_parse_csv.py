'''Problem 30: Write a python function parse_csv to parse csv (comma separated values) files.'''



import sys
def parse_csv(x):
	i=open(x).readlines()
	z=len(i)
	print [i[j].split(',') for j in range(0,z)]
parse_csv(sys.argv[1])	
