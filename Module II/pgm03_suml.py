#Problem 3: What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.


def sum(argv):
	result = " "
	for i in argv:
		result +=i
	return result
print sum(["aa","bb","cc"])

def sum(argv):
        result =""
        for i in argv:
           result +=i
        return result
print sum(["hello", "world"])

