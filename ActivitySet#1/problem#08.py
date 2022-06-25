# Files

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        x=line.lstrip("X-DSPAM-Confidence:")
        x=float(x)
        total=total+x
        
print("Average spam confidence:",total/count)


