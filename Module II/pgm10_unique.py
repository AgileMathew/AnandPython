#Write a function unique to find all the unique elements of a list.


def unique(x):
	result = []
	for i in x:
		if i not in result:
			result.append(i)
	return result
				
print unique([0,3,9,5,3,0,1,3])
