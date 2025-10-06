'''Escribe un programa que recoja un número y muestre un triángulo. Por
ejemplo, si se ha introducido el valor 5, se debe mostrar:
*
**
***
****
*****
'''
signo = "*"
fila = ""
filas = int(input("Introduzca el número de filas:"))
num = 0
while num < filas:
    fila += signo
    print(fila)
    num+=1