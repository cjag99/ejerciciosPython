'''10.Escribe un programa que recoja un número y muestre un triángulo formado por
secuencias decrecientes de números impares. Por ejemplo, si se introduce el
5 se debe mostrar:
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''
filas = int(input("Introduzca el nº de filas:"))
for c in range(filas):
    linea = []
    for n in range(c, -1, -1):
        linea.append(str(2 * n + 1))
    print(' '.join(linea))