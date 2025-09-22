'''2. Escribe un programa que recoja dos números enteros por teclado y muestre
los siguientes resultados: suma, resta, multiplicación, división real, división
entera, resto de la división entera y potencia.'''
num1 = int(input("Introduzca un número entero:"))
num2 = int(input("Ahora introduzca otro:"))
print("La suma de", num1, "y", num2, "es", num1+num2)
print("La resta de", num1, "y", num2, "es", num1-num2)
print("La multiplicación de", num1, "y", num2, "es", num1*num2)
print("La división real de", num1, "y", num2, "es", num1/num2)
print("La división entera de", num1, "y", num2, "es", num1//num2)
print("El resto de la división entera de", num1, "y", num2, "es", num1%num2)
print("La potencia de", num1, "elevado a", num2, "es", num1**num2)