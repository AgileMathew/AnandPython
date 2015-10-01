'''Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.'''



import sys
def parse(x,y,z):
	i=open(x).readlines()
	j=len(i)
	print [i[k].split(y) for k in range(0,j) if str(z) not in i[k]]

parse(sys.argv[1],sys.argv[2],sys.argv[3])
