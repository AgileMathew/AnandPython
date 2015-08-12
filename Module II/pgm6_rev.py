#Problem 6: Write a function reverse to reverse a list. Can you do this without using list slicing?


def rev(li):
#	return li[::-1]
#print rev([1,2,3,4])
#print rev(rev([1,2,3,4]))






def rev(li):
	a=[]
	for i in range((len(li)-1),-1,-1):
	  a.append(li[i])
	return a
print rev([1,2,3,4])
print rev(rev([1,2,3,4]))

