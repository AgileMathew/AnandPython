'''Python provides a built-in function map that applies a function to each element of a list.
Provide an implementation for map using list comprehensions.
'''


def square(x): return x*x

#map using list comprehensions
def my_map(func,list): return [func(i) for i in list]

print my_map(square, range(5))
print my_map(square, range(10,30,4))
