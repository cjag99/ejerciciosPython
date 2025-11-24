class Producto:
    def __init__(self, nombre, precio, descuento):
        if precio <= 0:
            raise ValueError("Error, el precio debe ser superior a 0€")
        if descuento < 0 or descuento > 1:
            raise ValueError("Error, valor no permitido de descuento")
        self.nombre = nombre
        self. precio = precio
        self.descuento = descuento

    def precio_final(self):
       return self.precio - (self.precio * self.descuento)