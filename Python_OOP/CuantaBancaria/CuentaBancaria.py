from Titular import Titular
class CuentaBancaria:
    def __init(self,titular:Titular, cantidad= 0.0):
        if titular is None:
            raise TypeError("Error, se debe proporcionar un titular")
        if not isinstance(titular, Titular):
            raise ValueError("Error, se debe proporcionar un titular válido")
        self.__titular = titular
        self.__cantidad = cantidad

    def setTitular(self, titular:Titular):
        if titular is None:
            raise TypeError("Error, se debe proporcionar un titular")
        if not isinstance(titular, Titular):
            raise ValueError("Error, se debe proporcionar un titular válido")
        self.__titular = titular
    
    def getTitular(self):
        return self.__titular
    
    def ingresar(self, cantidad):
        if cantidad < 0:
            raise ValueError("Error, no se pueden ingresar cantidades negativas")
        self.__cantidad+=cantidad
    
    def retirar(self, cantidad):
        self.__cantidad-= cantidad
    
    def getCantidad(self):
        return self.__cantidad

    def mostrar(self):
        return f"Titular: {self.getTitular().mostrar()}, Cantidad: {self.getCantidad()}€"
