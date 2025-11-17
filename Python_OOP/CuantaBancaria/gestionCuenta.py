from Titular import Titular
from CuentaBancaria import CuentaBancaria
from CuentaJoven import CuentaJoven

def crearTitular():
    print("Bienvenido/a a Banca Playamar.")
    while True:
        while True:
            print("Se le pedirán sus datos para poder verificar su identidad.")
            nombre = input("Por favor introduzca su nombre:")
            apellidos = input("Por favor introduzca sus apellidos")
            DNI = input("Por favor introduzca su DNI:")
            try:
                edad = int(input("Por favor, introduzca su edad:"))
                break
            except ValueError:
                print("Por favor introduzca un valor numérico")
            
            try:
                titular = Titular(nombre, apellidos, DNI, edad)
                print("Ha sido verificado. Bienvenido, ", titular.getNombre())
                return titular
            except ValueError as error:
                print(error)
                print("\nIntentelo de nuevo")



def crearCuentaBancaria(titular):
    print("A continuación procederemos con la creación de su cuenta Bancaria:")
    print("Identificando como titular de la cuenta...")
    if not titular:
        print("Error de identificación, cancelando operación...")
        return None
    
    print("Identificación exitosa")
    while True:
        try:
            cantidad = int(input("Por favor, introduzca si desea introducir una cantidad de dinero inicial:"))
            break
        except ValueError:
            print("Por favor introduzca un valor numérico")
    try:
        cuenta = CuentaBancaria(titular, cantidad)
        print("Cuenta Bancaria creada exitosamente")
        return cuenta
    except (TypeError, ValueError) as error:
        print(error)
        return None
    
        

def crearCuentaJoven(cuenta):
    if not cuenta:
        print("No se puede crear una Cuenta Joven sin una cuenta bancaria válida.")
        return None

    print("Vamos a verificar si puede usted ser beneficiario de la cuenta Joven.")
    while True:
        try:
            bonificacion = int(input("Por favor, introduzca el porcentaje de bonificacion que desea:"))
            break
        except ValueError:
            print("Por favor introduzca un valor numérico")
    
    try:
        cuentaJoven = CuentaJoven(cuenta, bonificacion)
        print("Cuenta Joven creada con éxito")
        return cuentaJoven
    except ValueError as error:
        print(error)
        return None

def menuCuenta():
    print("MENÚ DE OPCIONES:")
    print("a) Mostrar información de la cuenta")
    print("b) Mostrar saldo")
    print("c) Ingresar saldo")
    print("d) Retirar saldo")
    print("e) Cambiar de titular")
    print("f) Cerrar sesión")