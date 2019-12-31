name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line.rstrip()
    if not line.startswith('From '):
        continue
    line = line.split()
    word=line[5]
    time=word.split(':')
    hour=time[0]
    
#retreive/create/update
    counts[hour]=counts.get(hour,0)+1
    
lst=list()
for k, v in counts.items():
    #newtup = (v,k)
    lst.append((k, v))
    lst.sort()
for k, v in lst:
    print (k, v)

        