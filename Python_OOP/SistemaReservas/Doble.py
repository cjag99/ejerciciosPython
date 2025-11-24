import Habitacion

class Doble(Habitacion.Habitacion):
    def __init__(self, suplemento= 0):
        super().__init__(70)
        if suplemento not in (0,10):
            raise ValueError("Error, el suplemento solo puede ser de 10€")
        self.suplemento = suplemento

    def calcular_precio(self, noches):
        return self.precioBase * noches + self.suplemento