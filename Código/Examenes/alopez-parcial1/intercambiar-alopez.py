#Problema 4 alopez
def intercambiar(lista):
    if isinstance(lista,list):
        return intercambiar_aux(lista)
    else:
        return "Error no es de tipo lista"

def intercambiar_aux(lista):
    if lista==[]:
        return []
    else:
        return [lista[1]]+[lista[0]]+intercambiar_aux(lista[2:])
