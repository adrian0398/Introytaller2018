def aparece(num,dig) :
        if isinstance(num,int) and (num>0) and isinstance(dig,int)  and(dig>0) :
                return aparece_aux(num,dig)
        else:
                return "Error"
def aparece_aux (num,dig):
        if(num ==0): # Rojo
                return 0
        else: # Verde
                if((num%10)==dig):
                        return 1+ aparece_aux(num // 10,dig)
                else:
                        return aparece_aux(num // 10,dig)
