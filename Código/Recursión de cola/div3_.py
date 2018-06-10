def div3(num):
     if isinstance(num,int):
          return div3_aux(num,0,0)
     else:
          return "Error"

def div3_aux(num, resultado, contador):
     if num==0:
          return resultado
     else:
          if (num%10)%3!=0:
              return div3_aux(num//10,num%10*(10**contador)+resultado,contador+1)
          else:
               return div3_aux(num//10,resultado,contador)
