#Problem 17: Write a program reverse.py to print lines of a file in reverse order.


from sys import argv
def reverse(file):
  f=open(file,'r')
  lines=f.readlines() 
  for line in lines:
   # for i in range(len(line)-1,-1,-1):
  #    print line[i],
   print line[::-1]
reverse('she.txt')
