def traspuesta(matriz):
     if isinstance (matriz,list) and matriz !=0:
          return tras(matriz,len(matriz),len(matriz[0]),[],0,0,[])
def tras(matriz,lonfila,loncolum,imatriz,fila,columna,res):
     if fila==lonfila:
          return imatriz
     else:
          if columna==loncolum:
               return tras(matriz,lonfila,loncolum,imatriz+res  ,fila+1,0,[])
          else:
               return tras(matriz,lonfila,loncolum,imatriz,fila,columna+1,[[matriz[fila][columna]]+res])
