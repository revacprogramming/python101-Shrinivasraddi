#list 
fname = input('Enter File Name: ')
fh = open(fname)
romeo = list()
juliet = fh.read()
words = juliet.split()

for word in words:
    if word not in romeo:
        romeo.append(word)

romeo.sort()
print(romeo)
