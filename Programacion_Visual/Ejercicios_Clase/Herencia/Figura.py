from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, color):
        self.__color = color

    @abstractmethod
    def calcular_area(self):
        pass

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, nuevoColor):
        self.__color = nuevoColor

    def __str__(self):
        return f"La figura tiene un color {self.__color}"
