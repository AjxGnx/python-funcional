def calculadora(operacion):
    def suma(a, b):
        print(a+b)

    def resta():
        print(10-5)

    def mult():
        print(5*5)
    opciones = {
        'suma': suma,
        'resta': resta,
        'multiplicacion': mult
    }

    return opciones[operacion]


calculadora('suma')(10, 11)

###########################################################

lista = [1, 2, 3]


def potencia(n):
    return n ** 2


lista2 = list(map(potencia, lista))

print(lista2)

###########################################################

lista3 = list(map(lambda n: n**2, lista))

print(lista3)

###########################################################


def mi_decorador(funcion):
    def retorno():
        print("estoy en el decorador")
        mas_tarde = funcion()
        print("estoy al final")
        return mas_tarde
    return retorno


@mi_decorador
def saludar():
    print("hola")


saludar()

###########################################################


def mi_decorador2(funcion):
    def retorno2(*args):
        print("\nestoy en el decorador")
        mas_tarde = funcion(*args)
        print("estoy al final")
        return mas_tarde
    return retorno2


@mi_decorador2
def saludar2(nombre):
    print("hola " + nombre)


saludar2("Alirio")
