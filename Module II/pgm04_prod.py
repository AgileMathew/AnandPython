#Problem 4: Implement a function product, to compute product of a list of numbers.


def prod_list(x):
    prod = 1
    for i in x:
      prod = prod * i
    return prod
print prod_list([3,2,3])

