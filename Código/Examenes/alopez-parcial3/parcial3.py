class Examenpy:
    def __init__(self):
        pass
    def contar(self,num):
        longitud=0
        seguir=True
        while seguir:
            longitud+=1
            num=num//10
            if num<1:
                seguir=False
        print("tiene "+str(longitud)+" digitos")

    def ordenar(self,lista):
        longitud=len(lista)
        menor=lista[0]
        pos=0
        lista2=[]
        for i in range(len(lista)):
            for k in range (len(lista)):
                if menor>lista[k]:
                    menor=lista[k]
                    pos=k
            lista=lista[:k]+lista[(k+1):]
            lista2+=[menor]
        print(lista2)


    def multimatriz(self,matriz1,matriz2): #se le cambia el nonmbre ya que no es transpuesta si no multiplicacion
        filas1=len(matriz1)
        valor=len(matriz1[0])
        columnas2=len(matriz2[0])
        matriz_2=[] # se anade un guion bajo que se dejo como espacio
        for i in range(filas1):
            sumalist=[]
            for k in range(columnas2):
                suma=0
                for t in range(valor):
                    suma += matriz1[i][valor] * matriz2[valor][k] # para que funcione no es valor, es t
                sumalist+=[suma]
            matriz_2+=[sumalist]
        print(matriz_2)
           
