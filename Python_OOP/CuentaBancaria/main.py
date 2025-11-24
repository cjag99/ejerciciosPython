from Titular import Titular
from CuentaBancaria import CuentaBancaria
from CuentaJoven import CuentaJoven


def crear_titular():
    print("\n--- Crear Titular ---")
    while True:
        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        dni = input("DNI: ").strip()
        edad_str = input("Edad: ").strip()
        try:
            edad = int(edad_str)
            titular = Titular(nombre, apellidos, dni, edad)
            print(f"Titular verificado: {titular.getNombre()}\n")
            return titular
        except ValueError as e:
            print(f"Error: {e}. Inténtelo de nuevo.\n")


def crear_cuenta_bancaria(titular):
    print("\n--- Crear Cuenta Bancaria ---")
    if titular is None:
        print("No hay titular válido. Cancela creación de cuenta.")
        return None
    while True:
        entrada = input("Cantidad inicial (deje vacío para 0): ").strip()
        if entrada == "":
            cantidad = 0.0
            break
        try:
            cantidad = float(entrada)
            break
        except ValueError:
            print("Introduzca un número válido para la cantidad.")
    try:
        cuenta = CuentaBancaria(titular, cantidad)
        print("Cuenta bancaria creada con éxito.\n")
        return cuenta
    except Exception as e:
        print(f"Error creando cuenta: {e}")
        return None


def crear_cuenta_joven(cuenta):
    print("\n--- Crear Cuenta Joven (opcional) ---")
    if cuenta is None:
        print("No hay cuenta bancaria. No se puede crear Cuenta Joven.")
        return None
    try:
        edad = cuenta.getTitular().getEdad()
    except Exception:
        edad = None

    if edad is None or edad >= 25:
        print("No cumple el requisito de edad para Cuenta Joven (menor de 25).\n")
        return None

    while True:
        entrada = input("Porcentaje de bonificación (0-100): ").strip()
        try:
            bon = float(entrada)
            # Intentar crear la cuenta joven; manejar ambos posibles constructores
            try:
                cj = CuentaJoven(cuenta, bon)
                print("Cuenta Joven creada correctamente.\n")
                return cj
            except Exception:
                # intentamos con titular + bonificación si el constructor está definido así
                try:
                    cj = CuentaJoven(cuenta.getTitular(), bon)
                    print("Cuenta Joven creada correctamente.\n")
                    return cj
                except Exception as e:
                    print(f"No se pudo crear Cuenta Joven: {e}")
                    return None
        except ValueError:
            print("Introduzca un número válido para la bonificación.")


def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("a) Mostrar información de la cuenta")
    print("b) Mostrar saldo")
    print("c) Ingresar saldo")
    print("d) Retirar saldo")
    print("e) Cambiar de titular")
    print("f) Crear/Intentar Cuenta Joven")
    print("g) Cerrar sesión / Salir")


def main():
    titular = crear_titular()
    cuenta = crear_cuenta_bancaria(titular)
    cuenta_joven = None

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip().lower()
        if opcion == "a":
            if cuenta:
                try:
                    print(cuenta.mostrar())
                except Exception as e:
                    print(f"Error mostrando cuenta: {e}")
            else:
                print("No hay ninguna cuenta creada.")

        elif opcion == "b":
            if cuenta:
                try:
                    print(f"Saldo: {cuenta.getCantidad()} €")
                except Exception as e:
                    print(f"Error obteniendo saldo: {e}")
            else:
                print("No hay ninguna cuenta creada.")

        elif opcion == "c":
            if cuenta:
                entrada = input("Cantidad a ingresar: ").strip()
                try:
                    cantidad = float(entrada)
                    cuenta.ingresar(cantidad)
                    print(f"Ingresados {cantidad} € correctamente.")
                except ValueError:
                    print("Introduzca una cantidad numérica válida.")
                except Exception as e:
                    print(f"Error al ingresar: {e}")
            else:
                print("No hay ninguna cuenta para ingresar dinero.")

        elif opcion == "d":
            if cuenta:
                entrada = input("Cantidad a retirar: ").strip()
                try:
                    cantidad = float(entrada)
                    cuenta.retirar(cantidad)
                    print(f"Retirados {cantidad} €.")
                except ValueError:
                    print("Introduzca una cantidad numérica válida.")
                except Exception as e:
                    print(f"Error al retirar: {e}")
            else:
                print("No hay ninguna cuenta para retirar dinero.")

        elif opcion == "e":
            if cuenta:
                print("--- Cambiar Titular ---")
                nuevo = crear_titular()
                try:
                    cuenta.setTitular(nuevo)
                    print("Titular actualizado correctamente.")
                except Exception as e:
                    print(f"Error al cambiar titular: {e}")
            else:
                print("No hay ninguna cuenta para cambiar el titular.")

        elif opcion == "f":
            if cuenta_joven:
                print("Ya existe una Cuenta Joven asociada.")
            else:
                cuenta_joven = crear_cuenta_joven(cuenta)

        elif opcion == "g":
            print("Cerrando sesión. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Introduzca una letra entre a-g.")


if __name__ == "__main__":
    main()
