from Figura import Figura

class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.__base = base
        self.__altura = altura

    def calcular_area(self):
        return self.__base * self.__altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, nuevoTam):
        self.__base = nuevoTam

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, nuevoTam):
        self.__altura = nuevoTam


    def __str__(self):
        return f"tamaño de la altura {self.__altura} cm y la base {self.__base} cm y {super().__str__()}"
