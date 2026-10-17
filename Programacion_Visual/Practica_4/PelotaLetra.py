from Pelota import Pelota
import random

class PelotaLetra(Pelota):
    def __init__(self, identificador, participante):
        super().__init__(identificador, participante)
        self.__letra = 'X'
    
    def generarValor(self):
        letras = ["A", "B", "C", "D"]
        self.__letra = random.choice(letras)
    
    def pintarPelota(self):
        colores = ["Azul", "Verde", "Rojo"]
        self.color = random.choice(colores)
    
    def __str__(self):
        letra = str(self.__letra)
        return f"{super().__str__()}\nLetra: {letra}"

    @property
    def letra(self):
        return self.__letra