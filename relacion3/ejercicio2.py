#Escribe un programa que recoja un número y calcule su factorial.
num = int(input("Introduzca un número:"))
contador = 1
copia = num
while copia> 0:
    contador *= copia
    copia -= 1
print("El factorial de", num, " es ", contador)