'''Escribe un programa que recoja un número de filas y columnas, y muestre una
tabla con tantas filas y columnas como indicadas, numerando las celdas de
izquierda a derecha y de arriba abajo. Por ejemplo, si se introducen 2 filas y 3
columnas, se debe mostrar:
1 2 3
4 5 6'''
filas = int(input("Introduzca el números de filas:"))
columnas = int(input("Introduzca el número de columnas:"))
num = 1
for f in range(filas):
    for c in range(columnas):
        print(num, end= " ")
        num+= 1
    print()