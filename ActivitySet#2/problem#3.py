l=[]
t=tuple()
def get_cs():
  #s = input('Enter a sring')
  s='system=s;database=d;username=u;password=p'
  return s

def cs_to_lot(cs):
  y=cs.split(';')
  return y
def main():
  cs = get_cs()
  
  lot = cs_to_lot(cs)
  #print(lot)

  length = len(lot)
  #print(length)
  for i in range(length):
    #print(i)
    x = lot[i].split('=')
    #print(x)
    t=tuple(x)
    #print(t)
    l.append(t)
    #print(l)
  return l
  
if __name__ == '__main__':
    main()
print(l)
#python problem#3.py
#cd ActivitySet#2