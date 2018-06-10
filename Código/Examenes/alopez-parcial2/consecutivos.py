def consecutivos(matriz):
    if isinstance(matriz,list):
        return consecutivos_aux(matriz,len(matriz),0,0,1)
    else:
        return "Error"
def consecutivos_aux(matriz,longitud,lenfilas,lencolumnas,contador):
    if contador==longitud**2+1:
        return True
    else:
        if lenfilas==longitud:
            return False
        if matriz[lenfilas][lencolumnas]==contador:
            return consecutivos_aux(matriz,longitud,0,0,contador+1)
        if matriz[lenfilas][lencolumnas]!=contador:
            if lencolumnas==longitud:
                return consecutivos_aux(matriz,longitud,lenfilas+1,0,contador)
            else:
                return consecutivos_aux(matriz,longitud,lenfilas,lencolumnas+1,contador)
