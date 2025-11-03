#Definir una agenda telefónica como un diccionario
agenda = {
    "Juan Pérez": "555-1234",
    "María Gómez": "555-5678",
    "Luis Rodríguez": "555-8765"
}
#Menú de opciones
def menu():
    print("MENÚ DE OPCIONES:")
    print("a)Listado de teléfonos, usando el orden por defecto.")
    print("b)Listado de teléfonos por orden alfabético.")
    print("c)insertar un nuevo contacto.")
    print("d)Modificar el teléfono de un contacto.")
    print("e)Buscar un número de teléfono.")
    print("f)Eliminar un contacto.")
    print("g)Borrar el listín telefónico.")
    print("h)Salir.")

#Función para obtener la opción del usuario controlando que sea válida
def opcion_menu():
    opcion = input("Seleccione una opción (a-h): ").lower()
    while True:
        match opcion:
            case 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h':
                return opcion
            case _:
                opcion = input("Opción no válida. Seleccione una opción (a-h): ").lower()

#Funcion para obtener el listado de teléfonos por defecto
def listado_telefonos():
   if len(agenda) == 0:
       print("La agenda está vacía.")
       return
   
   for nombre, telefono in agenda.items():
       print(f"{nombre}-{telefono}")

#Función para obtener el listado de teléfonos ordenados alfabéticamente
def listado_telefonos_alfabetico():
    for nombre in sorted(agenda):
        print(f"{nombre}: {agenda[nombre]}")

#Función para insertar un nuevo contacto
def insertar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    if nombre in agenda:
        print("El contacto ya existe.")
        print("Desea actualizar el número de teléfono? (s/n)")
        respuesta = input().lower()
        if respuesta == 's':
            agenda[nombre] = telefono
            print(f"Número de teléfono de {nombre} actualizado con éxito.")
        else:
            print("No se realizaron cambios.")
    else:
        agenda[nombre] = telefono
        print(f"Contacto {nombre} añadido con éxito.")

#Función para modificar el teléfono de un contacto
def modificar_telefono():
    nombre = input("Ingrese el nombre del contacto a modificar: ")
    if nombre in agenda:
        nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
        agenda[nombre] = nuevo_telefono
        print(f"Número de teléfono de {nombre} modificado con éxito.")
    else:
        print("El contacto no existe.")
        print("Desea insertarlo como nuevo contacto? (s/n)")
        respuesta = input().lower()
        if respuesta == 's':
            telefono = input("Ingrese el número de teléfono: ")
            agenda[nombre] = telefono
            print(f"Contacto {nombre} añadido con éxito.")
        else:
            print("No se realizaron cambios.")

#Función para buscar un número de teléfono
def buscar_telefono():
    telefono = input("Ingrese el número de teléfono a buscar: ")
    encontrados = 0
    for num in agenda.values():
        if num == telefono:
            encontrados += 1
    if encontrados > 0:
        print(f"Se encontraron {encontrados} contacto(s) con el número {telefono}.")
        for nombre, num in agenda.items():
            if num == telefono:
                print(f"{nombre}")
    else:
        print("No se encontraron números de teléfono coincidentes.")

#Función para eliminar un contacto
def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado con éxito.")
    else:
        print("El contacto no existe.")

#Función para borrar el listín telefónico
def borrar_listin():
    print("¿Está seguro de que desea borrar todo el listín telefónico? (s/n)")
    respuesta = input().lower()
    if respuesta == 's':
        agenda.clear()
        print("Listín telefónico borrado con éxito.")
    else:
        print("No se realizaron cambios.")

#Programa principal
def main():
    menu()
    while True:
        opcion = opcion_menu()
        match opcion:
            case 'a':
                listado_telefonos()
            case 'b':
                listado_telefonos_alfabetico()
            case 'c':
                insertar_contacto()
            case 'd':
                modificar_telefono()
            case 'e':
                buscar_telefono()
            case 'f':
                eliminar_contacto()
            case 'g':
                borrar_listin()
            case 'h':
                print("Saliendo del programa.")
                break
        input("Presione cualquier tecla para continuar...")

#Ejecutar el programa principal
main()