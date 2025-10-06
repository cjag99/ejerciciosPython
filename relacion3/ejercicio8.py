'''Escribe un programa que recoja un número y calcule si es primo.'''
num = int(input("Introduzca un número:"))
cont = 2
esPrimo = True
if num < 2:
    print("No se puede determinar si un número menos de 2 es primo o no")
else:
    for c in range(cont,num, 1):
        if num % c == 0:
            esPrimo = False
    if esPrimo:
        print(num, "es primo")
    else:
        print(num, "no es primo")