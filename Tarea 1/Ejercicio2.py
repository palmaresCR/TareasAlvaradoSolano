from num2words import num2words


def num_to_str (par2):
    if type(par2)!= int:
        print("error. 422")
    else: 
        if par2 <= 99:
            if par2 >=0:
                letras= num2words(par2, lang='es')# falta colocar el guion bajo
                letras=letras.replace(' ','_')                     
                print(letras)
                print(type(letras))
            else:
                print("error. 500")
        else:
            print("error. 500") 
        
