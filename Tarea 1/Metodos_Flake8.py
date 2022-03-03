# ERR6 -1.6
from num2words import num2words


def string_work(par1):
    if type(par1) != str:  # comprobacion tipo de entrada
        return "error. 420"
    else:
        if (par1.isalpha()):  # comprobacion de contenido del string (si son letras)
            return par1.swapcase()  # cambia mayus por minus y viceversa
        else:
            return "error. 420"


def num_to_str(par2):
    if type(par2) != int:  # comprobacion tipo de entrada
        return "error. 422"

    else:
        if par2 < 0 or par2 >= 100:  # comprobacion rango de entrada
            NRD = "error. 500"
            return NRD
        else:
            # uso de libreria para leer y reescribir el numero
            letras = num2words(par2, lang='es')
            letras = letras.replace(' ', '_')  # aqui inserta el guion
            return letras
