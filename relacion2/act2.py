'''2. Escribe un programa que recoja un número por teclado y muestre el día de la
semana que es (1 = Lunes, 2 = Martes...). En caso de introducir un número
incorrecto, mostrará el mensaje “Día de la semana incorrecto”.'''
diaSemana = int(input("Introduzca un número del 1 al 7 y diré con que día de la semana corresponde:"))
if diaSemana > 0 and diaSemana <= 7:
    match diaSemana:
        case 1: print("Es lunes")
        case 2: print("Es martes")
        case 3: print("Es miércoles")
        case 4: print("Es jueves")
        case 5: print("Es viernes")
        case 6: print ("Es sábado")
        case 7: print ("Es domingo")
else:
     print("Día de la semana incorrecto")