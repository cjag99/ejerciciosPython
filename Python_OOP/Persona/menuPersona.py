from Persona import Persona
def menu():
    print("MENU DE OPCIONES:")
    print("a) Listado de contactos por orden alfabético.")
    print("b) Añadir un nuevo contacto.")
    print("c) Modificar un contacto.")
    print("d) Buscar un número de teléfono.")
    print("e) Eliminar un contacto.")
    print("f) Salir")

def seleccionarOpcion():
    while True:
        opcion = input("Introduzca una opcion(a-f):")
        match opcion:
            case "a"|"b"|"c"|"d"|"e"|"f":
                return opcion
            case _:
                print("Introduzca una opcón correcta del menú(a-f):")
    
    

def listarContactos(contactos):
    if len(contactos)== 0:
        print("Lista de contactos vacía")
    else:
        contactos.sort(key= lambda x: x.getNombre())
        for contacto in contactos:
            print(contacto.toString())
    
def addContacto(contactos):
    nombre = input("Introduzca el nombre del contacto:")
    direccion = input("Introduzca la direccion del contacto:")
    telefono = input("Introduzca el telefono del contacto:")
    if nombre != "" and direccion != "" and telefono != "":
        contactos.append(Persona(nombre, direccion, telefono))

def modificarContacto(contactos):
    busca = input("Introduzca el nombre del contacto a modificar:")
    for contacto in contactos:
         if contacto.compare(busca, contacto):
            print("Contacto encontrado: ", contacto.getNombre())
            newNombre = input("Introduzca el nuevo nombre:")
            newDireccion = input("Introduzca la nueva direccion:")
            newTelefono = input("Introduzca el nuevo teléfono:")
            if newNombre != "":
                contacto.setNombre(newNombre)
            if newDireccion != "":
                contacto.setDireccion(newDireccion)
            if newTelefono != "":
                contacto.setTelefono(newTelefono)
            print("Contacto actualizado")
            break

def buscarContacto(contactos):
    buscaTel = input("Introduzca el teléfono del contacto:")
    for contacto in contactos:
        if contacto.getTelefono() == buscaTel:
            print("Contacto encontrado:\n", contacto.toString())
        else:
            print("Contacto no encontrado")


def eliminarContacto(contactos):
    buscaDel = input("Introduzca el nombre del contacto a eliminar:")
    for contacto in contactos:
        if contacto.compare(buscaDel, contacto):
            contactos.remove(contacto)
            print("Contacto eliminado")
            break

        

def main():
    contactos= []
    while True:
        menu()
        opcion = seleccionarOpcion()
        match opcion:
            case "a":
                listarContactos(contactos)
            case "b":
                addContacto(contactos)
            case "c":
                modificarContacto(contactos)
            case "d":
                buscarContacto(contactos)
            case "e":
                eliminarContacto(contactos)
            case "f":
                del contactos
                print("Finalizando programa...")
                break
        input("Introduzca cualquier tecla para continuar")

main()