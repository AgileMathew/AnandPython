#Problem 16: Write a function extsort to sort a list of files based on extension.



def extsort(x):
  x.sort(key=lambda i: i.split('.')[1])
  return x

print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
  
    
