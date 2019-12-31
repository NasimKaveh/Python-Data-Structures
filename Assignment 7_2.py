# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    a=line.find(':')
    b=line[a+1:]
    c=float(b.rstrip())
    count = count + 1
    total = total + c
print ('Average spam confidence:', total/count)
    