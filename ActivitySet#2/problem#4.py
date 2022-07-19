l=[]
t=tuple()

def get_cs():
  #s=input('Enetr a string')
  s='system=s;database=d;username=u;passwd=p'
  return s


def cs_to_lot(cs):
  x=cs.split(';')
  ln=len(x)
  for i in range(ln):
    y=x[i].split('=')
    t=tuple(y)
    l.append(t)
  return l

def lot_to_cs(lot):
  """convert list of strings to connected string"""
  equal = '='
  separate = ';'
  ln=len(lot)
  for i in range(ln):
    lot[i]=equal.join(lot[i])
  newcs=separate.join(lot)
  return newcs
    
def main():
  cs=get_cs()
  lot=cs_to_lot(cs)  # convert connect string to list of tuples
  print(lot)
  
  newcs=lot_to_cs(lot)  # convert list of strings to connect string
  return print(newcs)


if __name__ == '__main__':
   main()


#  cd ActivitySet#2
#  python problem#4.py                
