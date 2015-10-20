"""Problem 38: Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique."""
def invertdict(a):
	d={}
	for key,value in a.items():
		d[value]=key
	print d
invertdict({'x':1,'y':2,'z':3})
