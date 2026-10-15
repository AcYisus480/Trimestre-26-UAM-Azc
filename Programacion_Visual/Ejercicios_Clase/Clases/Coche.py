# Clases con camelCase

class Coche:
    ruedas = 4
    def __init__(self, modelo, color, aceleracion, nombreDuenio):
        self.__modelo = modelo
        self.__color = color
        self.__aceleracion = aceleracion
        self.__velocidad = 0
        self.__duenio = nombreDuenio

    def acelerarCarro(self):
        self.__velocidad = self.__velocidad + self.__aceleracion

    def frenarCarro (self):
        self.__velocidad = 0

    @property
    def duenio(self):
        return self.__duenio

    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def color(self):
        return self.__color
    
    @property
    def aceleracion(self):
        return self.__aceleracion
    
    @property
    def velocidad(self):
        return self.__velocidad

    @duenio.setter
    def duenio(self, nuevoDuenio):
        self.__duenio = nuevoDuenio

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @aceleracion.setter
    def aceleracion(self, aceleracion):
        self.__aceleracion = aceleracion

    @color.setter
    def color(self, color):
        self.__color = color

    def __str__(self):
        return f"El Mal educado 😈😈😈 es de color " + self.__color
    