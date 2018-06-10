#Examen parcial 1 Alopez

#Problema 1

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

#Problema 2


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


#Problema 3

def contarConsonantes(texto):
    if isinstance(texto,str): #Se cambio String por str ya que es el que es válido en este caso
        return contarConsonantes_aux(texto)
    else:
        return "Error no es de tipo String"

def contarConsonantes_aux(texto):
    if texto=="":
        return 0
    else:
        if(texto[0]=='a') or (texto[0]=='e') or (texto[0]=='i') or (texto[0]=='o') or (texto[0]=='u'):
            return contarConsonantes_aux(texto[1:])
        else:
            return 1+ contarConsonantes_aux(texto[1:])

#Problema 4
def intercambiar(lista):
    if isinstance(lista,list):
        return intercambiar_aux(lista)
    else:
        return "Error no es de tipo lista"

def intercambiar_aux(lista):
    if lista==[]:
        return []
    else:
        return [lista[1]]+[lista[0]]+intercambiar_aux(lista[2:])
