#Función que muestra el menú
def menuUser():
    print("MENÚ DE OPCIONES:")
    print("a) Insertar usuario")
    print("b) Mostrar usuarios")
    print("c) Cerrar programa")

#Funcion para mostrar usuario y mostrar mensaje de confirmación si se inserta correctamente
def insertUsuario(lista, idUser):
    nombre = input("Introduzca su nombre:")
    edad = int(input("Introduzca su edad:"))
    direccion = input("Introduzca su dirección de residencia:")
    telefono = input("Introduzca su nº de teléfono")
    user = dict()
    user["nombre"] = nombre
    user["edad"] = edad
    user["direccion"] = direccion
    user["telefono"] = telefono
    lista[idUser] = user
    if idUser in lista:
        print(user["nombre"] + " tiene " + str(user["edad"]) + " años, vive en " + user["direccion"] + ", y su nº de teléfono es " + user["telefono"])
    else:
        print("Error al insertar usuario")

#Funcopm que muestre por pantalla todos los usuarios
def mostrarUsuarios(lista):
    for usuario in lista.items():
        print(usuario)
#Funcion que permite seleccionar la opción del menú
def seleccionarOpcionUser():
    opcion = input("Seleccione una opción (a-c): ").lower()
    while True:
        match opcion:
            case 'a' | 'b' | 'c' :
                return opcion
            case _:
                opcion = input("Opción no válida. Seleccione una opción (a-b): ").lower()


#Funcion que muestra el menú de opciones del programa del bazar
def menuBazar():
    print("MENÚ DE OPCIONES:")
    print("1. Venta total mensual de cada producto.")
    print("2. Producto más vendido y menos vendido del mes.")
    print("3. Ventas diarias del producto con mayor venta mensual.")
    print("4. Día con mayor cantidad de ventas para cada producto.")


#Función que calcula las ventas mensuales de cada producto
def getVentasMensuales(lista):
  
    ventasMes = dict()
    for producto, dias in lista.items():
        ventaSemanal = sum(dias.values())  # suma las ventas diarias
        ventasMes[producto] = ventaSemanal * 4  # calcula el total mensual

    
    return ventasMes

#Función que muestra por pantalla las ventas mensuales para cada producto
def mostrarVentasMensuales(lista):
    for producto in lista.keys():
        print(producto + ": " + str(lista[producto]))

#Función que devuelve el producto más vendido de una lista y su valor de ventas
def getMaxVentasMensuales(lista):
    productoMasVendido = dict()
    max_producto = max(lista, key=lista.get)
    productoMasVendido[max_producto] = lista[max_producto]
    return productoMasVendido

#Función que devuelve el producto menos vendido de una lista y su valor de ventas
def getMinVentasMensuales(lista):
    productoMenosVendido = dict()
    min_producto = min(lista, key=lista.get)
    productoMenosVendido[min_producto] = lista[min_producto]
    return productoMenosVendido


#Funcion que muestra las ventas diarias del producto más vendido
def mostrarVentasProductoMax(producto, lista):
    if producto in lista:
        print(producto + "-> " + str(lista[producto]))

#Función que muestra el día con más ventas para cada producto
def mostrarDiaMaxVentasPorProducto(lista):
    for producto, ventas in lista.items():
        dia_max = max(ventas, key=ventas.get)
        print(f"{producto}: {dia_max} -> {ventas[dia_max]}")

#Función que permita al usuario seleccionar la opcion del programa del bazar
def seleccionarOpcionBazar():
    opcion = input("Introduzca la opción que desea ejecutar (1-5):")
    while True:
        match opcion:
            case "1"| "2"|"3"|"4"|"5":
                return int(opcion)
            case _:
                print("No se reconoce esa opción")



