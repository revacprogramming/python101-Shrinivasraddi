# Dictionaries..

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
srg = open(name)
g=list()
rmg={}
for line in srg:
    if not line.startswith("From "):
        
        continue
    if line.startswith("From "):
        m=line.split()
        a=m[1]
    g.append(a)
for word in g:
    rmg[word]=rmg.get(word,0)+1
biggest=None
for word,s in rmg.items():
    if biggest is None or s>biggest:
        biggest=s
        bigword=word
print(bigword,biggest)