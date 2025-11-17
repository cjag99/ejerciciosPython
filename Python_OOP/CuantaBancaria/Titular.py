class Titular:
    def __init__(self, nombre, apellidos, DNI, edad):
        if nombre == "" or apellidos == "" or DNI == "":
            raise ValueError("Error, el parámetro no puede estar vacío")
        if type(edad) == float or edad <0:
            raise ValueError("Error, la edad debe ser un valor entero positivo")
        self.__nombre = nombre.upper()
        self.__apellidos = apellidos.upper()
        self.__DNI = DNI.upper()
        self.__edad = edad
    
    def setNombre(self, nombre):
        if nombre == "":
            raise ValueError("Error, el nombre no puede estar vacío")
        self.__nombre = nombre.upper()
    
    def setApellidos(self, apellidos):
        if apellidos == "":
            raise ValueError("Error, los apellidos no pueden estar vacíos")
        self.__apellidos = apellidos
    
    def setDNI(self, DNI):
        if DNI =="":
            raise ValueError("Error, el DNI no puede estar vacío")
        self.__DNI = DNI
    
    def setEdad(self, edad):
        if type(edad)== float or edad < 0:
            raise ValueError("Error, la edad debe ser un valor entero positivo")
        self.__edad = edad

    def getNombre(self):
        return self.__nombre
    
    def getApellios(self):
        return self.__apellidos

    def getDNI(self):
        return self.__DNI
    
    def getEdad(self):
        return self.__edad
    
    def mostrar(self):
        return f"Nombre: {self.getNombre()}, Apellidos: {self.getApellios()}, DNI: {self.getDNI()}, Edad: {self.getEdad()}"
    
    def mayorEdad(self):
        return self.getEdad()>18

    