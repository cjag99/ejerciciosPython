class Persona:
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def setTelefono(self, telefono):
        self.__telefono = telefono
    
    def compare(self, nombre, other):
        if not isinstance(other, type(self)):
            return False
        return nombre == self.getNombre() and self.getTelefono() == other.getTelefono()
    
    def toString(self):
        return f"Nombre: {self.getNombre()}, Dirección: {self.getDireccion()}, Teléfono: {self.getTelefono()}"
    