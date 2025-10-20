#Permite seleccionar el ejercicio a resolver, verificando que se introduce un valor correcto
def seleccionarOpcion():
    opcionesValidas = {1,2,3,4,5}
    opcion = int(input("Introduce el nº del ejercicio a mostrar (1-4):"))
    while opcion not in opcionesValidas:
        opcion = int(input("Por favor, debe introducir un nº entre 1 y 4:"))
    return opcion
# Recoge numeros y los añade a una lista hasta que se introduce el 0
def recogerNumeros():
    listaNum = []
    while True:
        num = int(input("Introduce un nº entero (0 para salir): "))
        if num== 0:
            break
        listaNum.append(num)
    return listaNum

#Recoge cadenas y los añade a una lista hasta que se introduce una cadena vacía
def recogerCadenas():
    listaCadena=[]
    while True:
        cadena = input("Introduce una cadena (Cadena vacía para salir):")
        if cadena == "":
            break
        listaCadena.append(cadena)
    return listaCadena

#Recoge una cadena y la devuelve, verificando antes que no esté vacía
def recogerTexto():
    cadenaVacia = True
    while cadenaVacia:
        cadena = input("Introduce una cadena de texto (No puede ser cadena vacía):")
        if cadena == "":
            cadena = input("Por favor, introduzca una cadena que no esté vacía")
        else:
            cadenaVacia = False
    return cadena

#Muestra por pantalla el menú
def menu():
    print("")
    print("MENÜ DE OPCIONES:")
    print("1- Escribe un programa que recoja números de teclado hasta que se introduce un cero." 
    " Luego debe mostrar la secuencia de números de tres modos:" 
        "a. En el orden en que se introdujeron."
        "b. En orden creciente."
        "c. En orden decreciente.")
    print("")
    print("2-Repite el ejercicio anterior, pero ahora lo que se leen son textos. La condición" 
    "de finalización será la cadena vacía.")
    print("")
    print("3- Escribe un programa lea un texto y determine si es un palíndromo. Procura" 
    "crear una función palindromo(s) -> Bool.")
    print("")
    print("4-Escribe un programa que lea dos textos y compruebe si una es palíndromo de" 
    "la otra. El programa debe preguntar si se desea comprobar teniendo en cuenta" 
    "mayúsculas/minúsculas o no.")
    print("")
    print("5- Salir del programa")

#Muestra una secuencia de 3 maneras distintas
def mostrarSecuencia(lista):
    print("Imprimiendo lista en orden de inserción:")
    for elemento in lista: 
        print(elemento)
    
    print("Imprimiendo lista ordenada:")
    for elemento in sorted(lista):
        print(elemento)
    
    print("Imprimiendo lista en orden inverso:")
    for elemento in sorted(lista, reverse=True):
        print(elemento)

#Muestra si una cadena es palíndroma 
def esPalindromo(cadena):
    palindromo = False
    if cadena == cadena[::-1]:
        palindromo = True
    return palindromo

#Compara 2 cadenas y muestra si son palíndromas entre sí
def cadenasPalindromas(cadena1, cadena2):
    palindromas = False
    if cadena1 == cadena2[::-1] or cadena2 == cadena1[::-1]:
        palindromas = True
    return palindromas

def ejecutarOpcion(opcion):
    match opcion:
        case 1:
            print("Ejecutando ejercicio 1....")
            lista = recogerNumeros()
            mostrarSecuencia(lista)
            next = input("Pulse cualquier tecla para continuar:....")
        case 2:
            print("Ejecutando ejercicio 2....")
            lista = recogerCadenas()
            mostrarSecuencia(lista)
            next = input("Pulse cualquier tecla para continuar:....")
        case 3:
            print("Ejecutando ejercicio 3....")
            texto = recogerTexto()
            print(texto + " es palíndromo? " + str(esPalindromo(texto)))
            next = input("Pulse cualquier tecla para continuar:....")
        case 4:
            print("Ejecutando ejercicio 4....")
            texto1 = recogerTexto()
            texto2 = recogerTexto()
            print("Son " + texto1 + " y " + texto2 +" palíndromos?: "+ str(cadenasPalindromas(texto1, texto2)))
            next = input("Pulse cualquier tecla para continuar:....")
        case 5:
            print("Finalizando programa......")

salida = False
while not salida:
    menu()
    opcion = seleccionarOpcion()
    ejecutarOpcion(opcion)
    if opcion == 5:
        salida = True



