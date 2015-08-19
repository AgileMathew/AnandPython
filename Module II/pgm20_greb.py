#Problem 20: Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.


import sys
def grep(filename):
  f= open(filename,'r+')
  line = f.readlines()
  for i in line:
    if sys.argv[2] in i:
      print i,
grep(sys.argv[1])
      
