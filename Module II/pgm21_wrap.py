'''Problem 21: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.'''




import sys
f = open(sys.argv[1])
line = f.readlines()
wrap = int(sys.argv[2])
for i in line:
	print i[0:wrap] +  '\n' + i[wrap:]
