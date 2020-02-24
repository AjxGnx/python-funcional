"""
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. 
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta 
de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los
descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta."""


def descuento(precio, p_descuento):
    return precio - ((precio * p_descuento)/100)


def iva(precio, p_iva):
    return precio + ((precio * p_iva)/100)


precios = {
    12000: 20,
    20000: 10,
    30000: 17,
    5000:  15,
    19000: 16
}


def precio_final(lista_precios, funcion):
    total = 0
    for precio, porcentaje in lista_precios.items():
        total += funcion(precio, porcentaje)
    return total


print("el valor final de la canasta con descuentos es: {} ". format(
    precio_final(precios, descuento)))

print("el valor final de la canasta con iva es: {} ". format(
    precio_final(precios, iva)))
