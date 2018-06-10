def multiplicacion(matriz1,matriz2):
    if isinstance (matriz1,list) and matriz1!=0 and isinstance (matriz2,list) and matriz2!=0:
        return crearm(matriz1,matriz2,len(matriz1),len(matriz2[0]),0,0,[],[])
    else:
        return "Error"
                      
                              
def crearm(matriz1,matriz2,n,m,fila,columna,newmatriz,filamatriz):
    
    if fila==n:
        return newmatriz
    else:
        if columna==m:
            return crearm(matriz1,matriz2,n,m,fila+1,0,newmatriz+[filamatriz],[])
        else:
            return crearm(matriz1,matriz2,n,m,fila,columna+1,newmatriz,filamatriz+[multimatrix(matriz1,matriz2,0,0,0,fila,columna)]) # pasar numero fila

def multimatrix(matriz1,matriz2,valor,suma,multiplicacion,fila,columna):
    suma=suma+multiplicacion

    if len(matriz1[0])==valor:
        return suma
    else:
        return multimatrix(matriz1,matriz2,valor+1,suma,matriz1[fila][valor]*matriz2[valor][columna],fila,columna)
        
        
    
                           
                
            
    
