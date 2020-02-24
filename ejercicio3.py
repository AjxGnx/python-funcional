"""
escribir que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
"""


def diccionario(frase):
    diccionario = {}
    for i in frase.split():
        diccionario[i] = len(i)
    return diccionario


print(diccionario("welcome to the jungle"))
