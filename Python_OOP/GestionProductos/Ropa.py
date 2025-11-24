import Producto

class Ropa(Producto.Producto):
    def __init__(self, nombre, precio, descuento):
        if descuento < 0 or descuento > 0.2:
             raise ValueError("Error, el descuento para este producto no puede ser negativo ni superar el 20%")
        super().__init__(nombre, precio, descuento)