from Pelota import Pelota
import random

class PelotaNumero(Pelota):
    def __init__(self, identificador, participante):
        super().__init__(identificador, participante)
        self.__numero = 0
    
    def generarValor(self):
        self.__numero = random.randint(1, 4)
            
    def pintarPelota(self):
        colores = ["Amarillo", "Morado", "Rosa"]
        self.color = random.choice(colores)

    def __str__(self):
        num = str(self.__numero)
        return f"{super().__str__()}\nNúmero: {num}"

    @property
    def numero(self):
        return self.__numero
