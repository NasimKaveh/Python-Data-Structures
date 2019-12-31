name = input("Enter file:")
counts = dict()
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
    #line = line.rstrip()
    if not line.startswith('From:'):
        continue
    line = line.split()
    email = line[1]
    #print(email)
    counts[email] = counts.get(email,0) + 1
#print (counts)

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print (bigword, bigcount)
