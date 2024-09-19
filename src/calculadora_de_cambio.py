import math

def converter(valor, taxa):

    resultado = valor * taxa
    resultado = math.floor(resultado * 100) / 100
    
    return resultado