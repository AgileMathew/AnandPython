#Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively

import sys
def head(filename):
  f=open(filename).readline()
  print f[0:10]
def tail(filename):
  temp=len(open(filename).readline())
  z=open(filename).readline()
print z[temp-10:temp]



print "head first 10 lines"
x=head(sys.argv[1])
print "tail for "
