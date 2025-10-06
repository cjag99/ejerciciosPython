#Definición funciones de ejercicioFunciones.py
def mostrarRombo():
    errorFlag = True
    while errorFlag:
        try:
            num = int(input("Introduce un número impar: "))
            if num % 2 == 1:
                    errorFlag = False
            else:
                    print("El número no es impar. Inténtalo de nuevo.")
            for i in range(1, num + 1, 2): 
                espacios = (num - i) // 2  
                print(" " * espacios + "*" * i)
            for f in range(num-2,0, -2):
                espacios = (num - f) // 2  
                print(" " * espacios +"*" * f)
        except ValueError:
            print("ERROR, no se ha introducido un número válido")


def adivinarNum():
     import random
     randNum =random.randint(1, 100)
     if randNum < 50:
          print("El número es menor a 50")
     else:
          print("El número es mayor a 50")
     acierto = False
     numIntentos = 0
     while acierto == False:
        try:
            num = int(input("Intenta adivinar el número entero entre 1 y 100:"))
            numIntentos+=1
            if num == randNum:
                print("Enhorabuena, has acertado")
                print("Nº intentos:", numIntentos)
                acierto = True
            else:
                print("Error, vuelve a intentarlo")
        except ValueError:
            print("ERROR, no se ha introducido un número válido")


def resolverEcuacion():
    import math
    try:
        valorA = int(input("Introduzca el primer coeficiente:"))
        valorB = int(input("Introduzca el segundo coeficiente:"))
        valorC = int(input("Introduzca el tercer coeficiente:"))       
        if valorA==0:
            if valorB == 0:
                if valorC== 0:
                    print("La ecuación tiene infinitas soluciones: 0=0")
                else:
                    print("La ecuación no tiene soluciones reales")
            else:
                valorX = -valorC / valorB
                print("La ecuación solo tiene una solución:", valorX)
        else:
            discriminante = valorB**2 - (4*valorA*valorC)
            if discriminante < 0:
                print("La ecuación no tiene soluciones reales")
            elif discriminante == 0:
                print("La ecuación solo tiene un valor:", -valorB)
            else:
                valorX1 = -valorB + math.sqrt(discriminante)
                valorX2 = -valorB - math.sqrt(discriminante)
                print("La ecuación tiene 2 soluciones: X1=", valorX1, " X2=", valorX2)
    except ValueError:
        print("ERROR, no se ha introducido un número válido")

def tablaNumeros() :
    import random
    try:
        columnas = int(input("Introduzca el nº de columnas de la tabla:"))
        filas = int(input("Introduzca el nº de filas de la tabla:"))
        for  _ in range(filas):
            for _ in range(columnas):
                print(random.randint(1,10), end = " ")
            print()
    except ValueError:
        print("ERROR, no se ha introducido un número válido")

def factorial():
    import math
    try:
        num = int(input("Introduzca el nº para calcular su factorial:"))
        if num < 1:
            print("ERROR, no se puede calcular el factorial de números menores de 1")
        else:
            print("El factorial de", num, "es", math.factorial(num))
    except ValueError:
        print("ERROR, no se ha introducido un número válido")

def fibonacci():
    try:
        num = int(input("Introduzca el nº para calcular su sucesión de Fibonacci:"))
        sucesion = [1,1]
        for num in range(1, num+1, 1):
            sucesion.append((sucesion[sucesion.__len__()-1] + sucesion[sucesion.__len__()-2]))
            for d in range(0, sucesion.__len__(), 1):
                print(sucesion[d], end = " ")
            print()
    except ValueError:
        print("ERROR, no se ha introducido un número válido")

def tablaMultiplicar():
    try:
        num = int(input("Indique un nº natural para mostrar su tabla de multiplicar:"))
        if num < 0:
            print("Error,", num, "no es positivo. Debe ser un número natural")
        else:
            for n in range(0,11, 1):
                print(num, "*", n, "=", (num*n))
    except ValueError:
        print("ERROR, no se ha introducido un número válido")