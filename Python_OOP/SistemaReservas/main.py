from Individual import Individual
from Doble import Doble
from Suite import Suite

def main():
    # Crear solo instancias válidas. Las clases gestionan su propio precio base.
    try:
        habitaciones = [
            Individual(),
            Doble(suplemento=10),
            Suite(),
        ]
    except Exception as e:
        print(f"Error creando habitaciones: {e}")
        return

    # Definir noches por tipo de habitación de forma clara y sin 'trucos'
    reservas = []
    for h in habitaciones:
        if isinstance(h, Individual):
            noches = 2
        elif isinstance(h, Doble):
            noches = 4
        elif isinstance(h, Suite):
            noches = 5
        else:
            noches = 1
        reservas.append((h, noches))

    total = 0.0
    for habitacion, noches in reservas:
        try:
            if not isinstance(noches, int) or noches <= 0:
                raise ValueError("El número de noches debe ser un entero positivo")

            precio = habitacion.calcular_precio(noches)

            if not isinstance(precio, (int, float)):
                raise TypeError("El precio calculado debe ser numérico")
            if precio < 0:
                raise ValueError("El precio calculado no puede ser negativo")

            print(f"{habitacion.__class__.__name__}: {noches} noches -> {precio:.2f}€")
            total += precio
        except Exception as e:
            print(f"Error calculando precio para {habitacion.__class__.__name__}: {e}")

    print(f"Precio total: {total:.2f}€")


if __name__ == '__main__':
    main()
