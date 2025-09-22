'''3. Escribe un programa que lea tres números y que muestre los números mayor
y menor.'''
num1 = int(input("Introduzca un número:"))
num2 = int(input("Introduzca otro número:"))
num3 = int(input("Introduzca un último número:"))
if num1>num2 and num1>num3:
    if num2>num3:
        print(num1, "es el mayor y", num3, "el menor")
    else:
        print(num1, "es el mayor y", num3, "el menor")
elif num2>num1 and num2>num3:
    if num1>num3:
        print(num2, "es el mayor y", num3, "el menor")
    else:
        print(num2, "es el mayor y", num1, "el menor")
else:
    if num1>num2:
        print(num3, "es el mayor y", num2, "el menor")
    else:
        print(num3, "es el mayor y", num1, "el menor")