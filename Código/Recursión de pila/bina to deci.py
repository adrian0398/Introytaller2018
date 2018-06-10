def cantidad_list(a):
     if a == []:
          return 0
     elif isinstance(a, list):
          return cont_lis_aux(a)
     else:
          return "Debe ser lista"
def conta_lis_aux(a):
     return 1 + conta_lis_aux(a[1:])
               
