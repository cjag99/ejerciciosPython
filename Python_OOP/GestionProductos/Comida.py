import Producto

class Comida(Producto.Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, 0)