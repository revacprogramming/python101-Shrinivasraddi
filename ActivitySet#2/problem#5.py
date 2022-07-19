dic={}
def get_cs():
    #s = input('input a string')
    s = 'system=s;database=d;username=u;password=p'
    return s
  
def cs_to_dict(cs):
    """convert connect string to a dictionary"""
    x=cs.split(';')
    for i in x:
        y = i.split('=')
        dic[y[0]] = y[1]
    return dic
def dict_to_cs(d):
    """convert a dictionary to connect string"""
    str=""
    for x in d:
      # str=str+x+'='+d[x]+';'
        str=';'.join(key +'='+ value for key, value in d.items())
    return str
def main():
    cs = get_cs()
    d = cs_to_dict(cs)
    print(d)
    
    cs = dict_to_cs(d)
    print(cs)

if __name__ == '__main__':
    main()