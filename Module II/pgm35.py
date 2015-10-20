"""Problem 35: Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?"""



def word_frequency(words):
	frequency={}
	for w in words:
		frequency[w]=frequency.get(w, 0)+1
	return frequency
def main(filename):
    frequency = word_frequency(read_words(filename))
    for word, count in frequency.items():
        print word, count

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
