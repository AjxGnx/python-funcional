"""
Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, 
tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función 
a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el 
resultado de aplicar la función a esos enteros."""

from math import sin, cos, tan, exp, log


def calculadora(operacion, valor):
    opciones = {
        "sin": sin,
        "cos": cos,
        "tan": tan,
        "exp": exp,
        "log": log
    }

    result = {}

    for i in range(1, valor+1):
        result[i] = opciones[operacion](i)
    return result


def result():
    operacion = input(
        "introduce el nombre de la operacion a realizar (sin, cos, tan, exp, log): ")
    valor = int(input("introduce el valor a calcular: "))

    for key, value in calculadora(operacion, valor).items():
        print(key, "->", value)
    return


result()
