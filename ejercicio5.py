"""
Escribir una función reciba un diccionario con la las asignaturas y las notas de un alumno y 
devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes
a las notas."""


def diccionario_notas(notas_alumno):
    result = {}
    for key, value in notas_alumno.items():
        result[key.title()] = nota_to_calificacion(value)

    return result


notas = {
    "matematica": 10,
    "ingles": 9,
    "castellano": 2,
    "quimica": 6,
    "fisica": 5,
    "deporte": 3
}


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


print(diccionario_notas(notas))
