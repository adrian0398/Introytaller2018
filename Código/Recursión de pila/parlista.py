def par(lista):
     if isinstance(lista,list):
          return par_aux(lista)
     else: return "Error"

def par_aux(lista):
     if lista==[]:
          return 0
     else:
          if lista[0]%2==0:
               return lista[0] + par_aux(lista[1:])
          else:
               return par_aux(lista[1:])
          
