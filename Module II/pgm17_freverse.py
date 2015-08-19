#Write a program reverse.py to print lines of a file in reverse order.

from sys import argv
def reverse(file):
   f=open(file,'r')
   lines = f.readlines()
   lines.reverse()
   for line in lines:
      print line

reverse(argv[1])
