'''4. Escribe un programa que recoja dividendo y divisor, y realice su división
siempre que el divisor sea distinto de cero.'''
dividendo= int(input("Introduzca un numero entero(dividendo):"))
divisor = int(input("Introduzca otro número entero(divisor). Debe ser distinto a 0:"))
if divisor != 0:
    print("El resultado de la división es", dividendo/divisor)
else:
    print("No se puede dividir entre 0")