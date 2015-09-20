'''Problem 22: The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?'''




from sys import argv
lines=open(argv[1]).readlines()
wrap=int(argv[2])
for line in lines:
        if line[wrap]!=' ':
                prev_space=line[:wrap].rfind(' ')+1
                print line[:prev_space] + '\n' + line[prev_space:]
        else:
                print line[:wrap] + '\n' + line[wrap:]
