#Dado un numero,determine su longitud
#Entrada: es un numero entero
#Restricciones; es un numero entero positivo mayor a cero
#Salida: longitud de un numero
def longitud(num) :
        if isinstance(num,int) and (num>0):
                return longitud_aux(abs(num))
        else:
                return "Error"
def longitud_aux (num):
        if(num ==0): # Rojo
                return 0
        else: # Verde
                return num %10 -(num%10-1)+ longitud_aux(num // 10)
