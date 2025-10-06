'''Usa funciones para escribir de forma sencilla un programa con las siguientes
instrucciones:
1. Al arrancar debe mostrar un menú de opciones como el siguiente:
MENÚ DE OPCIONES
a) Mostrar un rombo.
b) Adivinar un número.
c) Resolver una ecuación de segundo grado.
d) Tabla de números.
e) Cálculo del número factorial de un número.
f) Cálculo de un número de la sucesión de Fibonacci.
g) Tabla de multiplicar.
h) Salir'''

#Definiendo función del menú
def ejecutarOpcion(letra):
    import funciones
    match letra:
        case "A"|"a":
            funciones.mostrarRombo()
        case "B"|"b":
            funciones.adivinarNum()
        case "C"|"c":
            funciones.resolverEcuacion()
        case "D"|"d":
            funciones.tablaNumeros()
        case "E"|"e":
            funciones.factorial()
        case "F"|"f":
            funciones.fibonacci()
        case "G"|"g":
            funciones.tablaMultiplicar()
        case "H"|"h":
            print("Finalizando programa...")
            exit()
        case _:
            print("ERROR, esa opción no está en el menú.")
while True:
    print("MENÚ DE OPCIONES")
    print("a) Mostrar un rombo.")
    print("b) Adivinar un número.")
    print("c) Resolver una ecuación de segundo grado.")
    print("d) Tabla de números.")
    print("e) Cálculo del número factorial de un número.")
    print("f) Cálculo de un número de la sucesión de Fibonacci.")
    print("g) Tabla de multiplicar.")
    print("h) Salir.")
    letra = input("Introduzca que opción desea ejecutar:")
    ejecutarOpcion(letra)
   
    
