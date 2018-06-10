def multilista(lista):
     if isinstance(lista,list):
          return mult(lista,1)
     else: "Error"

def mult(lista,resultado):
     if lista==[]:
          return resultado
     else:
          return mult(lista[1:],lista[0]*resultado)
