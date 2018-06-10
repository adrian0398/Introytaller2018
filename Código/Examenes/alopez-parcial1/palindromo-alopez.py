#Problema 2 alopez
def palindromo(num):
    if isinstance(num,int) and num>0:
        return validar(num)
    else:
        return "Error no es un entero positivo mayor que 0"

def palindromo_aux(num,exp): #se anaden 2 puntos que no se pusieron en el examen
    if num==0:
        return 0
    else:
        return (num%10)*(10**(exp-1))+palindromo_aux(num//10,exp-1)

def long(num):
    if num==0:
        return 0
    else:
        return 1+ long(num//10)

def validar(num):
    if num== palindromo_aux(num,long(num)):
        return True
    else:
        return False
