def sumapot(lista):
     if isinstance(lista,list):
          return suma(lista,1)
     else: return "Error"

def suma(lista,n):
     if lista==[]:
          return 0
     else:
          if isinstance(lista[0],list):
               return suma(lista[0],n)+suma(lista[1:],len(lista[0])+n)
          else:
               return lista[0]**n+suma(lista[1:],n+1)
