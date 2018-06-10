#Problema 3 alopez

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
