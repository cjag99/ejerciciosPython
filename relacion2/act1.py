'''1. Escribe un programa que recoja un número e indique si se trata de un número
par o impar.'''
num = int(input("Introduzca un número entero y te diré si es par o impar:"))
if num %2 ==0:
    print(num, "es par")
else:
    print(num, "es impar")