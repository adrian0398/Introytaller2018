def sumatoria2 (num):

  if isinstance (num,int) and (num>0):

    return sumatoria2_aux(abs(num))

  else:

    return "Error"

  def sumatoria2_aux (num):

    if (num==0):

      return 0 

    else:

      return num+5*(num*num)**2 + sumatoria2_aux(num-1)
