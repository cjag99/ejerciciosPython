from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, modelo, anyo):
        self.modelo = modelo
        self.anyo = anyo

    @abstractmethod
    def calcular_consumo(self, kilometros):
        pass