import Vehiculo

class Moto(Vehiculo.Vehiculo):
    def __init__(self, modelo, anyo):
        super().__init__(modelo, anyo)

    def calcular_consumo(self, kilometros):
        return (kilometros * 3)/100