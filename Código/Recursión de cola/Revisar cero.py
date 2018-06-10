def revisar_cero(num):
     if isinstance(num, list):
          listacero = lambda dig : dig == 0
          return revisar_cero_aux(num, listacero)
     else:
          return "No es una lista"

def revisar_cero_aux(num, condicion):
     if num == []:
          return False
     elif condicion(num[0]):
          return True
     else:
          return revisar_cero_aux(num[1:], condicion)
          
