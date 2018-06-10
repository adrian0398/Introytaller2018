def rotar(matriz):
    if isinstance(matriz,list):
        return rotar_aux(matriz,len(matriz),len(matriz[0]),0,0,[],[])
    else:
        return "Error"

def rotar_aux(matriz,lencolumnas,lenfilas,filas,columnas,rotada,newfila):
    if columnas==lencolumnas:
        return rotada
    else:
        if lenfilas==filas:
            return rotar_aux(matriz,lenfilas,lencolumnas,0,columnas+1,rotada+newfila,[])
        else:
            return rotar_aux(matriz,lenfilas,lencolumnas,filas+1,columnas,rotada,newfila+[matriz[filas][columnas]])
