# ERR 4x2 -5
# ERR5x2 -6: No prueba todo el rango de letras, no prueba todos los números
# de 0 a 99
import pytest
from Metodos import*


# Una prueba que verifica que el método string_work es capaz de cambiar todos los caracteres de a-Z. Verificando tanto mayúsculas como minúsculas.
def test_letras():
    temp = string_work("AbCdefG")
    assert temp == ("aBcDEFg")

# Una prueba que verifica que el método string_work retorna el error correcto si se le pasa un número como entrada.


def test_numeros():
    temp2 = string_work("420")
    assert temp2 == "error. 420"

# Una prueba que verifica que el método string_work retorna el error correcto si se le pasa un string con números y/o símbolos.


def test_simbolos():
    temp3 = string_work("@")
    assert temp3 == "error. 420"


# Una prueba que verifica que el método num_to_str puede traducir todos los números desde el 0 al 99 correctamente.
def test_traducir():
    temp4 = num_to_str(54)
    assert temp4 == "cincuenta_y_cuatro"


def test_traducir1():
    temp5 = num_to_str(99)
    assert temp5 == "noventa_y_nueve"

# Una prueba que verifica que el método num_to_str retorna el error correcto si se le pasa un string.


def test_string():
    temp6 = num_to_str("string")
    assert temp6 == "error. 422"

# Una prueba que verifica que el método num_to_str retorna el error correcto si se le pasa un número negativo, deciaml o mayor a 99.


def test_numeros_negativos():
    temp7 = num_to_str(-99)
    assert temp7 == ("error. 500")


def test_numeros_mayores():
    tempx = num_to_str(100)
    assert tempx == ("error. 500")


def test_numeros_decimales():
    temp8 = num_to_str(54.9)
    assert temp8 == ("error. 422")
