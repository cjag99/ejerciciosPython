import Producto

class Electrodomestico(Producto.Producto):
    def __init__(self, nombre, precio, descuento):
        if descuento < 0 or descuento > 0.1:
            raise ValueError("Error, el descuento para este producto no puede ser negativo ni superar el 10%")
        super().__init__(nombre, precio, descuento)