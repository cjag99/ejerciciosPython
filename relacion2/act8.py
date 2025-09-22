'''8. Escribe un programa que recoja un mes del año (en número) y devuelva el
número de días que tiene el mes. En caso de indicar un mes incorrecto deberá
mostrar un mensaje de error.'''
numMes = int(input("Introduzca el número del mes y te diré cuantos días tiene:"))
if numMes >=1 and numMes < 13:
    match numMes:
        case 4|6|9|11:
            print("Tu mes tiene 30 días")
        case 1|3|5|7|8|10|12:
            print("Tu mes tiene 31 días")
        case 2:
            print("Tu mes puede tener 28 o 29 días(depende de si el año es bisiesto o no)")
else:
    print("ERROR:", numMes, "no corresponde con un mes válido(1-12)")