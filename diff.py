import sys

corpusLines = None

corpusMap = dict()

with open(sys.argv[1]) as corpus:
        for line in corpus:
                corpusMap[line] = 1

for line in sys.stdin:
        key = line.split()[]
        if key not in corpusMap:
                print key