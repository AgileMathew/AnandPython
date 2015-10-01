'''Problem 28: Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.'''


def enumerate(item):
	index = range(len(item))
	return zip(index,item)
for index, value in enumerate(["a", "b", "c"]):
     	print index, value

