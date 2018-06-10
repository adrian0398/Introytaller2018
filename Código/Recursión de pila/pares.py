def pares_aux(Num):
     string = str(Num)
     lista = list(string)
     if lista[-1] % 2 == 0:
          return lista[-1] + pares_aux(Num//10)
     else:
          return pares_aux(Num//10)
