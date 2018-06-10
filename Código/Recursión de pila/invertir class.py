class Invertir:

     def  _init_(self):
          pass
     def inv(self,lista):
          if isinstance(lista,list):
               return self.inv1(lista)
          else:
               return "Error"

     def inv1(self,lista):
          if lista==[]:
               return []
          else:
               return [lista[-1]] + self.inv1(lista[:-1])         
