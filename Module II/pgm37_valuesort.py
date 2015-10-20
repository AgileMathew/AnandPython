"""Problem 37: Write a function valuesort to sort values of a dictionary based on the key."""
def valuesort(a):
	d={}
	result=[]
	d=a.keys()
	for key,value in a.items():
		d.sort()
	
	for i in d:
		result.append(a[i])
	print result
valuesort({'x':1,'y':2,'a':3})
