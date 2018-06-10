def es_magico(matriz):
    if isinstance(matriz,list):
        return cuadradomagico(matriz,len(matriz),0,0)
    else:
        return "Error"
def sumadiagonal(matriz,lenmatriz,filas,suma):
    if filas==lenmatriz:
        return suma
    else:
        return sumadiagonal(matriz,lenmatriz,filas+1,matriz[filas][filas]+suma)

def antidiagonal(matriz,
                              
