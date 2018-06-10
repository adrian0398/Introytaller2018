def sumaypromediomatriz(matriz):
     if isinstance (matriz,list) and matriz !=0:
          return suma(matriz,len(matriz),len(matriz[0]),0,0,0)
def suma(matriz,lonfila,loncolum,suma1,fila,columna):
     if fila==lonfila:
          return (suma1,suma1/(loncolum*lonfila))
     else:
          if columna==loncolum:
               return suma(matriz,lonfila,loncolum,suma1,fila+1,0)
          else:
               return suma(matriz,lonfila,loncolum,matriz[fila][columna]+suma1,fila,columna+1)
