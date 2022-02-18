#import pytest
#import row_to_list

#def test_for_clean_row():
#   assert row_to_list() == \ []


def string_work(par1): 
    if type(par1)!= str: #validacion tipo str
        print("error. 420")                    
    else:
        if (par1.isalpha()): #validación simbolo y caracter
            print(par1.swapcase()) #Invierte mayusculas y minusculas
        else:
            print("error. 420")
