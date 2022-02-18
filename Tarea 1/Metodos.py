from num2words import num2words

def string_work(par1):
   if type(par1)!= str:
      return "error. 420"
      print("error. 420")
   else:
      if (par1.isalpha()):
         return par1.swapcase()
         print (par1.swapcase())
      else:
         return "error. 420"
         print("error. 420")
    

def num_to_str (par2):
   print(par2)
   if type(par2)!= int: #comprobación tipo de entrada  
      print("error. 422")    
      return "error. 422"

   else:
      if par2 < 0 or par2 >= 100:#comprobación rango de entrada
         NRD = "error. 500"
         print(NRD)
         return NRD
      
      #if par2 >= 100:#comprobación rango de entrada
      #   NRD2 = "error. 501"
      #   print(NRD2)
      #   return NRD2

      else:
         letras= num2words(par2, lang='es')#uso de librería para leer y reescribir el número
         letras=letras.replace(' ','_') #aquí inserta el guión                     
         print(letras)
         return letras      
