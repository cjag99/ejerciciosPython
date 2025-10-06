'''Escribe un programa que recoja un número impar. Debe asegurarse de que
sea impar, en caso de no serlo debe descartarlo y pedirlo de nuevo. Una vez
tenga el número impar debe mostrar una pirámide de asteriscos cuya base es
igual al número introducido. Por ejemplo, si se introduce el valor 7 se debe
mostrar:
*
***
*****
******* <- base de la pirámide (7 asteriscos)'''
errorFlag = True

while errorFlag:
        num = int(input("Introduce un número impar: "))
        if num % 2 == 1:
            errorFlag = False
        else:
            print("El número no es impar. Inténtalo de nuevo.")


for i in range(1, num + 1, 2): 
    espacios = (num - i) // 2  
    print(" " * espacios + "*" * i)
