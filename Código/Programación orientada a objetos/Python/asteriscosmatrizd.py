class AsteriscosMatriz:
     def _init_(self):
          pass
     def asteriscos(self,n):
          if isinstance(n,int):
               return self.crear(n,[],[],0,0)
          else:
               return "Error"
     def crear(self,n,matriz,valor,fila,columna):
          if fila==n:
               return matriz
          else:
               if columna==n:
                    return self.crear(n,matriz+[valor],[],fila+1,0)
               if fila==0 or fila==(n-1):
                     return self.crear(n,matriz,valor+["*"],fila,columna+1)
               if columna==0 or columna==(n-1):
                    return self.crear(n,matriz,valor+["*"],fila,columna+1)
               else:
                    return self.crear(n,matriz,valor+["0"],fila,columna+1)


                    
     
