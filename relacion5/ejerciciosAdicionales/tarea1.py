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

#Devuelve una lista con el menor y mayor elemento de la lista dada
def rango(lista):
    if len(lista) == 0:
        raise ValueError("Error: La lista no puede estar vacía")
    else:
        menor = min(lista)
        mayor = max(lista)
        
    return [menor, mayor]
#Devuelve una lista sin los extremos de la lista dada
def interior(lista):
    if len(lista) < 2:
        raise ValueError("Error: La lista debe tener al menos 2 elementos")
    else:
        return lista[1:-1]
#Devuelve una lista con los n últimos elementos de la lista dada, controlando que n no sea mayor que la longitud de la lista
def finales(n, lista):
    if n > len(lista):
        raise ValueError(f"Error: {n} es mayor que {len(lista)}")
    elif n < 0:
        raise ValueError(f"Error: {n} no equivale a una posición válida")
    else:
        return lista[-n:]
#Devuelve una lista con los elementos comprendidos entre las posiciones m y n, controlando que m y n sean válidos
def segmento(m, n, lista):
    if m < 0 or n < 0 or m >= len(lista) or n > len(lista):
        raise ValueError("Error: Las posiciones no son válidas")
    elif m >= n:
        return []
    else:
        return lista[m:n]
#Devuelve una lista con los n primeros y n últimos elementos de la lista dada, controlando que n no sea mayor que la longitud de la lista
def extremos(n, lista):
    if n > len(lista):
        raise ValueError(f"Error: {n} es mayor que {len(lista)}")
    elif n < 0:
        raise ValueError(f"Error: {n} no equivale a una posición válida")
    else:
        return lista[:n] + lista[-n:]
#Devuelve la tupla que representa el rectángulo de mayor área entre las dos dadas
def mayorRectangulo(r1, r2):
    area1 = r1[0] * r1[1]
    area2 = r2[0] * r2[1]
    if area1 >= area2:
        return r1
    else:
        return r2
#Devuelve la tupla con las coordenadas intercambiadas
def intercambia(p):
    return (p[1], p[0]) 

#Programa principal
def main():
    menu()
    while True:
        opcion = seleccionarOpcion()
        
        if opcion == 0:
            print("Saliendo del programa...")
            break
        elif opcion == 1:
            cadena = recogerCadena()
            numVocales = contarVocales(cadena)
            print(f"La cadena tiene {numVocales} vocales.")
        elif opcion == 2:
            cadena = recogerCadena()
            numPalabras = contarPalabras(cadena)
            print(f"La cadena tiene {numPalabras} palabras.")
        elif opcion == 3:
            num1 = recogerNumero()
            num2 = recogerNumero()
            num3 = recogerNumero()
            suma1 = sumar(num1, num2)
            sumaTotal = sumar(suma1, num3)
            print(f"La suma de los tres números es: {sumaTotal}")
        elif opcion == 4:
            num = recogerNumero()
            lista = recogerLista()
            try:
                listaRotada = rota(num, lista)
                print(f"La lista rotada es: {listaRotada}")
            except ValueError as e:
                print(e)
        elif opcion == 5:
            lista = recogerLista()
            try:
                rangoLista = rango(lista)
                print(f"El rango de la lista es: {rangoLista}")
            except ValueError as e:
                print(e)
        elif opcion == 6:
            lista = recogerLista()
            try:
                listaInterior = interior(lista)
                print(f"La lista interior es: {listaInterior}")
            except ValueError as e:
                print(e)
        elif opcion == 7:
            n = recogerNumero()
            lista = recogerLista()
            try:
                listaFinales = finales(n, lista)
                print(f"Los últimos {n} elementos de la lista son: {listaFinales}")
            except ValueError as e:
                print(e)
        elif opcion == 8:
            m = recogerNumero()
            n = recogerNumero()
            lista = recogerLista()
            try:
                segmentoLista = segmento(m, n, lista)
                print(f"El segmento de la lista es: {segmentoLista}")
            except ValueError as e:
                print(e)
        elif opcion == 9:
            n = recogerNumero()
            lista = recogerLista()
            try:
                listaExtremos = extremos(n, lista)
                print(f"Los extremos de la lista son: {listaExtremos}")
            except ValueError as e:
                print(e)
        elif opcion == 10:
            print("Introduzca las dimensiones del primer rectángulo:")
            r1 = recogerTupla()
            print("Introduzca las dimensiones del segundo rectángulo:")
            r2 = recogerTupla()
            mayorRect = mayorRectangulo(r1, r2)
            print(f"El rectángulo de mayor área es: {mayorRect}")
        elif opcion == 11:
            print("Introduzca las coordenadas del punto:")
            p = recogerTupla()
            puntoIntercambiado = intercambia(p)
            print(f"El punto con las coordenadas intercambiadas es: {puntoIntercambiado}")
        else:
            print("Opción no válida.")
            
        input("Pulse cualquier tecla para continuar...")



main()