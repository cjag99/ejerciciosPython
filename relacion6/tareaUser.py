import funciones
usuarios = dict()
numUser = 1
#Función principal del programa
def main():
    global numUser
    funciones.menuUser()
    while True:
        opcion = funciones.seleccionarOpcionUser()
        match opcion:
            case 'a':
                funciones.insertUsuario(usuarios, ("user" + str(numUser)))
                numUser+=1
            case 'b':
                funciones.mostrarUsuarios(usuarios)
            case 'c':
                print("Finalizando programa...")
                break
        input("Pulse cualquier tecla para continuar...")


main()