"""
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones
correspondientes a esas notas.
https://internacional.ugr.es/pages/conversion-calificaciones/tablaconversioncalificaciones/!"""


def calificaciones(notas):
    return list(map(nota_to_calificacion, notas))


def nota_to_calificacion(nota):
    if nota < 5:
        return 'SS'
    elif nota < 7:
        return 'AP'
    elif nota < 9:
        return 'NT'
    elif nota < 10:
        return 'SB'
    else:
        return 'MH'


print(calificaciones([3, 5, 9, 10, 2, 5, 8]))
