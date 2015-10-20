"""Problem 34: Improve the above program to print the words in the descending order of the number of occurrences."""


def word_frequency(words):
	frequency = dict()
	for w in words:
		frequency[w] = frequency.get(w, 0) + 1
	return frequency

def read_words(filename):
    return open(filename).read().split()

def sortfunc(x):
		return x[1]

def main(filename):
	frequency = sorted(word_frequency(read_words(filename)).items(),key=sortfunc,reverse=True)
	for word, count in frequency:
		print word, count

if __name__ == '__main__':
	from sys import argv
	main(argv[1])
