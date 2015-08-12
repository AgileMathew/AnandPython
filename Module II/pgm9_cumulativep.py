#Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.




def cumulative_prod(x):
	result = [x[0]]
	for i in range(1,len(x)):
		result.append(result[-1]*x[i])
	return result
print cumulative_prod([1,2,3,4])
