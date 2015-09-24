def even(x):
	return x %2 == 0
def filter(f, a):return [item for item in a if f(item)]

print filter(even,range(10))
