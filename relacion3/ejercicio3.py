'''Escribe un programa que recoja números por teclado hasta que se introduzca
el valor cero. A continuación, debe mostrar el número de valores introducidos,
el valor mínimo introducido, el máximo, la suma de todos ellos y su media
aritmética (todos los cálculos sin contar el cero)'''
num=1
array1 = []
suma = 0
while num !=0:
    num = int(input("Introduce un número:"))
    array1.append(num)
array1Sorted = sorted(array1)
array1Sorted.remove(0)
for d in array1Sorted:
    suma += d

media = suma / array1Sorted.__len__()
print("Números introducidos:", array1.__len__())
print("Valor mínimo:", array1Sorted[0])
print("Valor máximo:", array1Sorted[array1Sorted.__len__()-1])
print("Suma de sus valores:", suma)
print("Media aritmética de sus valores:", media)