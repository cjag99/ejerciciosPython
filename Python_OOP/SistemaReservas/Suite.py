import Habitacion

class Suite(Habitacion.Habitacion):
    def __init__(self):
        super().__init__(150)

    def calcular_precio(self, noches):
       if noches > 3:
          return (self.precioBase * noches) - ((self.precioBase * noches) * 0.1)
       else:
          return self.precioBase * noches