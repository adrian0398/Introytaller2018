def cero (lista):
     if isinstance(lista,list):
          return cero_aux(lista)
     else: return "Error"

def cero_aux(lista):
     if lista==[]:
          return False
     else:
          if lista[0]==0:
               return True
          else:
               return cero_aux(lista[1:])
          
