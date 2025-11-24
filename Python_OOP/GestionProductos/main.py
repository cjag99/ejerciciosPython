from Comida import Comida
from Ropa import Ropa
from Electrodomestico import Electrodomestico

def main():
    productos = []

    try:
        productos.append(Comida("Pan", 1.20))
    except ValueError as e:
        print(f"Error creando 'Pan': {e}")

    try:
        productos.append(Comida("Leche", 0.99))
    except ValueError as e:
        print(f"Error creando 'Leche': {e}")

    try:
        productos.append(Ropa("Camiseta", 20.00, 0.15))
    except ValueError as e:
        print(f"Error creando 'Camiseta': {e}")

    try:
        productos.append(Ropa("Pantalones", 40.00, 0.10))
    except ValueError as e:
        print(f"Error creando 'Pantalones': {e}")

    try:
        productos.append(Electrodomestico("Microondas", 80.00, 0.05))
    except ValueError as e:
        print(f"Error creando 'Microondas': {e}")

    try:
        productos.append(Electrodomestico("Tostadora", 30.00, 0.00))
    except ValueError as e:
        print(f"Error creando 'Tostadora': {e}")

    for producto in productos:
        print(f"{producto.nombre}: precio final = {producto.precio_final():.2f} €")

if __name__ == "__main__":
    main()
