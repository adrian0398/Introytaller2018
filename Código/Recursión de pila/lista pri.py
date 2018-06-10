def listapri(lista):
     if isinstance(lista,list):
          return reco(lista)
     else:
          return "Error"

def reco(lista):
     if lista==[]:
          return []
     else:
          if pri1(lista[0])==True:
               return [lista[0]]+reco(lista[1:])
          else:
               return reco(lista[1:])
def pri1(num):
     if isinstance(num,int) and num>=0 :
          return pri(num,num-1)
     else:
          return "Error"
     
def pri(num,divisor):
     if (divisor==1) or (num==1):
          return True
     else:
          if (num%divisor)==0:
               return False
          else:
               return pri(num, divisor-1)
