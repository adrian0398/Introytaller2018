def intercambiar(num):
     if isinstance(num,int):
          cero=lambda digito: digito!=0
          return inte(num,cero,0)
     else:
          return "Error"
def inte(num,comb,er):
   # if(comb(num%10) and comb(num%100//10)):
     if num==0
          return 0
          else:
               return ((num%10)*(10**(er+1)))+(((num%100)//10) *(10**er)) + inte(num//100,comb,er+2)


     
