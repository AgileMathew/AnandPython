def enumerate(item):
	index = range(len(item))
	return zip(index,item)
for index, value in enumerate(["a", "b", "c"]):
     	print index, value

