def repite(lista,num):
     if isinstance(num,int) and isinstance(lista,list):
          rep=lambda digito : digito==num
          return repite_aux(lista,rep)
     else: "Error"
def repite_aux(lista,condicion):
     if lista==[]:
          return 0
     else:
          if condicion(lista[0]):
               return 1+ repite_aux(lista[1:],condicion)
          else:
               return repite_aux(lista[1:],condicion)
