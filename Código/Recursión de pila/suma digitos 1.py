def suma_digitos(num) :
        if isinstance(num,int) and (num>0):
                return suma_digitos_aux(abs(num))
        else:
                return "Error"
def suma_digitos_aux (num):
        if(num ==0): # Rojo
                return 0
        else: # Verde
                return num % 10 + suma_digitos_aux(num // 10)
        
