#Muestra por pantalla el menú
def menu():
    print("")
    print("1- Definir una función que, al recibir una cadena de texto, cuente cuántas vocales hay y"
          "devuelva dicho valor.")
    print("")
    print("2- Definir una función que, al recibir una cadena de texto, cuente cuántas palabras hay y"
          "devuelva dicho valor.")
    print("")
    print("3- Definir una función que devuelva la suma dos números. Utilizar esa función para sumar tres números.")
    print("")
    print("4- Definir la función"
          " rota : (int, List[A]) -> List[A]"
          "tal que rota(n, xs) es la lista obtenida poniendo los n primeros"
          "elementos de xs al final de la lista. Por ejemplo,"
          "rota(1, [3, 2, 5, 7]) == [2, 5, 7, 3]"
          "rota(2, [3, 2, 5, 7]) == [5, 7, 3, 2]"
          "rota(3, [3, 2, 5, 7]) == [7, 3, 2, 5]")
    print("")
    print("5- Definir la función"
          "rango : (List[int]) -> List[int]"
          "tal que rango(xs) es la lista formada por el menor y mayor elemento"
          "de xs."
          "rango([3, 2, 7, 5]) == [2, 7]")
    print("")
    print("6- Definir la función"
          "interior : (list[A]) -> list[A]"
          "tal que interior(xs) es la lista obtenida eliminando los extremos de"
          "la lista xs. Por ejemplo,"
          "interior([2, 5, 3, 7, 3]) == [5, 3, 7]")
    print("")
    print("7- Definir la función"
          "finales : (int, list[A]) -> list[A]"
          "tal que finales(n, xs) es la lista formada por los n finales"
          "elementos de xs. Por ejemplo,"
          "finales(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]")
    print("")
    print("8- Ejercicio 13. Definir la función"
          "segmento : (int, int, list[A]) -> list[A]"
          "tal que segmento(m, n, xs) es la lista de los elementos de xs"
          "comprendidos entre las posiciones m y n. Por ejemplo,"
          "segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]"
          "segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]"
          "segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []")
    print("")
    print("9- Definir la función"
          "extremos : (int, list[A]) -> list[A]"
          "tal que extremos(n, xs) es la lista formada por los n primeros"
          "elementos de xs y los n finales elementos de xs. Por ejemplo,"
          "extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]) == [2, 6, 7, 9, 2, 3]")
    print("")
    print("10- Las dimensiones de los rectángulos puede representarse"
          "por pares; por ejemplo, (5,3) representa a un rectángulo de base 5 y"
          "altura 3."
          "Definir la función"
          "mayorRectangulo : (tuple[float, float], tuple[float, float])"
          "-> tuple[float, float]"
          "tal que mayorRectangulo(r1, r2) es el rectángulo de mayor área entre"
          "r1 y r2. Por ejemplo,"
          "mayorRectangulo((4, 6), (3, 7)) == (4, 6)"
          "mayorRectangulo((4, 6), (3, 8)) == (4, 6)"
          "mayorRectangulo((4, 6), (3, 9)) == (3, 9)")
    print("")
    print("11- Definir la función"
          "intercambia : (tuple[A, B]) -> tuple[B, A]"
          "tal que intercambia(p) es el punto obtenido intercambiando las"
          "coordenadas del punto p. Por ejemplo,"
          "intercambia((2,5)) == (5,2)"
          "intercambia((5,2)) == (2,5)")
    
#Permite seleccionar el ejercicio a realizar, controlandoq que se introduzca una opción válida
def seleccionarOpcion():
    opcionesValidas = {1,2,3,4,5,6,7,8,9,10,11,0}
    opcion = int(input("Introduzca que ejercicio desea realizar(1-11, 0 para salir): "))
    while opcion not in opcionesValidas:
        opcion = int(input("Debe introducir una opción válida(1-11, 0 para salir):"))
    
    return opcion

#Recoge un nº distinto a 0
def recogerNumero():
    while True:
        num = int(input("Introduzca un nº entero distinto a 0:"))
        if num != 0:
            break
    return num

#Recoge una lista de números, finalizando cuando se introduce 0
def recogerLista():
    listaNum = []
    while True:
        num = int(input("Introduzca un nº entero (0 para salir):"))
        if num == 0:
            break
        listaNum.append(num)
    return listaNum

#Recoge una tupla de 2 valores float
def recogerTupla():
    import math
   
    while True:
        num1 = float(input("Introduzca un nº:"))
        num2 = float(input("Introduzca otro nº:"))
        if not math.isnan(num1) or not math.isnan(num2):
            break
        tupla = (num1, num2)
    return tupla

#Recoge una cadena de texto no vacía
def recogerCadena():
    while True:
        cadena = input("Introduzca una cadena no vacía:")
        if cadena != "":
            break
    return cadena

#Cuenta cuantas vocales hay en una cadena y devuelve el valor
def contarVocales(cadena):
    numVocales = 0
    vocales = {"a","e","i","o","u"}
    for letra in cadena:
        if letra in vocales:
            numVocales +=1

    return numVocales

#Cuentas cuantas palabras hay en una cadena y devuelve el valor
def contarPalabras(cadena):
    palabras = cadena.split()
    numPalabras = len(palabras)
    return numPalabras

#Suma 2 números y devuelve el valor
def sumar(num1, num2):
    return num1 + num2

#Rota el nº de elementos indicados en la lista al final de la misma y la devuelve, controlando que no se indique un nº mayor a la longitud de la misma
def rota(num, lista):
    if num > len(lista):
        raise ValueError(f"Error: {num} es mayor que {len(lista)}")
    elif num < 0:
        raise ValueError(f"Error: {num} no equivale a una posición válida")
    elif num == len(lista):
        return lista
    else:
        copiaLista = [lista.pop(0) for _ in range(num)]
        lista.extend(copiaLista)
        
    return lista


        



