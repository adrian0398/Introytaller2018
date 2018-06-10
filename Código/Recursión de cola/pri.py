def primo(num):
     if(num>=0) and isinstance(num,int):
          return pri(num,num-1)
     else:
          return "Error"
     

def pri(num,num1):
     if(num<=1) :
          return  "El número es Especial"
     else:
          if(num1==1):
               return "El número es Primo"
               
          if ((num % num1)==0):
               return "El número es Compuesto"
          else:
               return pri(num,num1-1)
