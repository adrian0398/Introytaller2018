class Valoresingresados:
    def __init__(self):
        pass
        
    def suma(self):
        salir=True
        suma1=0
    
        while salir:
            num=int(input("Introduzca numeros, 0 para detener"))
            suma1+=num
            if num==0:
                salir=False
        return suma1
            
            
        
