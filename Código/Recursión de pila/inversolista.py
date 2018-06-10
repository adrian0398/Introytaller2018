def inv(lista):
     if isinstance(lista,list):
          return inv1(lista)
     else:
          return "Error"

def inv1(lista):
     if lista==[]:
          return []
     else:
          return [lista[-1]] + inv1(lista[:-1])         
