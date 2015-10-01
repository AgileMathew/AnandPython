'''Problem 29: Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:'''

import sys
def array(i,j):
	return [['none']*j for x in range(0,i)]
print array(int(sys.argv[1]), int(sys.argv[2]))

