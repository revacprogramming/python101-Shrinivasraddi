# Regular Expressions
# https://www.py4e.com/lessons/rege x
# Dictionaries..
import re

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
maggy = open(name)
g=list()
maharshi={}
for line in maggy:
  m=re.search("From ")
  m=line.split()
  if len(m)>0:
    a=m[1]
    g.append(a)
for word in g:
    maharshi[word]=maharshi.get(word,0)+1
biggest=None
for word,s in maharshi.items():
    if biggest is None or s>biggest:
        biggest=s
        bigword=word
print(bigword,biggest)
