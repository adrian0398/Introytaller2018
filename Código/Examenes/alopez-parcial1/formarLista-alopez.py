#Problema 1 alopez
def formarLista(num):
    if isinstance(num,int) and (num>0):
        return formarLista_aux(num)
    else:
        return "Error no es un entero positivo mayor que 0"

def formarLista_aux(num):
    if num==0:
        return []
    else:
        if ((num%10)%2)==0:
            return formarLista_aux(num//10)+[num%10]
        else:
            return formarLista_aux(num//10)
