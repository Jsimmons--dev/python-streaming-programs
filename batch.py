import sys

batch=[]
batchSize=sys.argv[1]
counter=0
joiner=','

for line in sys.stdin:
        if counter < int(batchSize):
                batch.append(line.rstrip())
                counter+=1
        else:
                print joiner.join(batch)
                batch=[line.rstrip()]
                counter=1

if len(batch) > 0:
        print joiner.join(batch)