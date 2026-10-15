from Figura import Figura

class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.__lado = lado

    def calcular_area(self):
        return self.__lado * self.__lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, nuevoTam):
        self.__lado = nuevoTam

    def __str__(self):
        return f"tamaño del lado {self.__lado} y {super().__str__()}"