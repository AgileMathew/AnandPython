#Problem 7: Python has built-in functions min and max to compute minimum and maximum of a given list. Provide an implementation for these functions. What happens when you call your min and max functions with a list of strings?



def min_list(x):
  min_element=x[0]
  for i in range(1,len(x)):
    if min_element>x[i]:
      min_element = x[i]
  return min_element

print min_list([6,5,8,4,3])

def max_list(x):
  max_element = x[0]
  for i in range(1,len(x)):
    if max_element<x[i]:
      max_element = x[i]
  return max_element
print max_list([10,267,13,444,56])
