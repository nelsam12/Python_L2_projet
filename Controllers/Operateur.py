import random

from Models.Operateur import save_operator

def generer_numeros_telephones(prefixe, index, nombre, longueur=7):
    numeros = []
    for _ in range(nombre):
        numero = (
            str("") + str(index) + 
            "".join(str(random.randint(0, 9)) for _ in range(longueur))
        )
        numeros.append(numero)
    return numeros

def add_operator(operator):
    save_operator(operateur=operator)