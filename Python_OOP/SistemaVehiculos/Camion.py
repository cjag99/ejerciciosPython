import Vehiculo

class Camion(Vehiculo.Vehiculo):
    def __init__(self, modelo, anyo):
        super().__init__(modelo, anyo)

    def calcular_consumo(self, kilometros, carga):
        if carga >= 1:
            return ((kilometros*20)/100) + carga * (((kilometros*20)/100)* 0.1)
        else:
            return ((kilometros*20)/100)