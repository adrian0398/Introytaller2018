def invertir(lista):
    if isinstance(lista,list) and lista!=[]:
        return invertir_aux(lista,len(lista),0)
    else:
        return "Error"
def invertir_aux(lista,longitud,indices):
    if longitud==indices:
        return lista[:longitud]
    else:
        return ([lista[indices]]+lista,longitud,indices+1)
