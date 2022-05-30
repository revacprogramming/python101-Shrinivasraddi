# Tuples

#filename = "dataset/mbox-short.txt"
file = open('mbox-short.txt')
di={}
for line in file:
    if line.startswith('From '):
        line.rstrip
        words=line.split()
        w=words[5]
        
        k=w[:2]
        di[k]=di.get(k,0)+1 

t=[]
for key,value in di.items():
    t.append((key,value))
t=sorted(t)
for key,value in t:
    print (key,value)


