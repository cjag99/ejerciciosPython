from CuentaBancaria import CuentaBancaria
from Titular import Titular


class CuentaJoven(CuentaBancaria):
    def __init__(self, owner, bonificacion):
        # owner can be a CuentaBancaria or a Titular
        if isinstance(owner, CuentaBancaria):
            titular = owner.getTitular()
            cantidad = owner.getCantidad()
        else:
            titular = owner
            cantidad = 0.0

        super().__init__(titular, cantidad)

        if not isinstance(titular, Titular):
            raise ValueError("Error, se debe proporcionar un titular válido")

        if titular.getEdad() >= 25:
            raise ValueError("Error, la Cuenta Joven está reservada para clientes menores de 25 años")

        if bonificacion < 0 or bonificacion > 100:
            raise ValueError("Error: formato inválido de porcentaje de bonificación")

        self.__bonificacion = bonificacion
    
    def setBonificacion(self, bonificacion):
        if bonificacion < 0 or bonificacion > 100:
            raise ValueError("Error: formato inválido de porcentaje de bonificación")
        self.__bonificacion = bonificacion
    
    def getBonificacion(self):
        return self.__bonificacion
        
    def mostrar(self):
        return f"Cuenta Tipo Joven: {super().mostrar()}, Bonificación: {self.getBonificacion()}"