import Habitacion

class Individual(Habitacion.Habitacion):
    def __init__(self):
        super().__init__(50)

    def calcular_precio(self, noches):
        return self.precioBase * noches