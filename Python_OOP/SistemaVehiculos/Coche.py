import Vehiculo

class Coche(Vehiculo.Vehiculo):
    def __init__(self, modelo, anyo):
        super().__init__(modelo, anyo)

    def calcular_consumo(self, kilometros):
        return (kilometros *5)/100