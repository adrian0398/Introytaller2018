class Binariodecimal:
    def _init_(self):
        pass

    def binarioadecimal(self,num,a):
        if num==0:
            return 0
        else:
            if num%10==1:
                return 2**(a)+ self.binarioadecimal(num//10,a+1)
            else:
                return self.binarioadecimal(num//10,a+1)

    def binario(self,num):
        if isinstance(num,int):
            return self.binarioadecimal(num,0)
        else:
            return "Error"


    def decimal(self,num):
        if isinstance(num,int):
            return self.decimalabinario(num,0)
        else:
            return "Error"
    
    def decimalabinario(self,num,a):
        if num==0:
            return 0
        else:
            if (num)%2==0:
                return self.decimalabinario((num//2),a+1)+ 0*10
            else:
                return self.decimalabinario((num//2),a+1)+ 1*(10**a)
        

