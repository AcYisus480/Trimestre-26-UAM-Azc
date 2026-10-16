from abc import ABC, abstractmethod

class Pelota(ABC):
    def __init__(self, identificador, participante):
        self.__identificador = identificador
        self.__participante = participante
        self.__color = "Blanco"
    
    @abstractmethod
    def pintarPelota(self):
        pass
    
    @abstractmethod
    def generarValor(self):
        pass
    
    def __str__(self):
        nombre = self.__participante
        id_usuario = str(self.__identificador)
        color = self.__color
        return f"Participante: {nombre}\nID: {id_usuario}\nColor: {color}"
    
    @property
    def color(self):
        return self.__color

    @property
    def identificador(self):
        return self.__identificador

    @property
    def participante(self):
        return self.__participante