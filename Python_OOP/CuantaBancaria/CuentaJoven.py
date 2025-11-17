from CuentaBancaria import CuentaBancaria
class CuentaJoven(CuentaBancaria):
    def __init__(self, cuenta: CuentaBancaria, bonificacion):
        super.__init__(cuenta)
        if cuenta.getTitular.getEdad() >25:
            raise ValueError("Error, la cuenta Joven está reservada para clientes menores de 25 años")
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
        return f"Cuenta Tipo Joven: {super.mostrar()}, Bonificación: {self.getBonificacion()}"