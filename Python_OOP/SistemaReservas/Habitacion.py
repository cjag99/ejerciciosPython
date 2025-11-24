from abc import ABC, abstractmethod

class Habitacion(ABC):
    def __init__(self, precioBase):
        self.precioBase = precioBase

    @abstractmethod
    def calcular_precio(self, noches):
        pass