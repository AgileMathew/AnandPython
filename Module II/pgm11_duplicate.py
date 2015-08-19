#Problem 11: Write a function dups to find all duplicates in the list.
def dups(x):
  z = []
  y = []
  for i in x:
    if i not in z:
      z.append(i)
    else:
      y.append(i)
  return y
print dups([1,2,1,2,3,4,5])
#def dups(x):
#  result = []
#  y = []
#  for i in x:
#    if i not in result:
#      result.append(i)
#    else:
#      y.append(i)
#  return y
#print dups([1, 2, 1, 3, 2, 5])
