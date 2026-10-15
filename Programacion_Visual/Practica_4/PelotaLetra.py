from Pelota import Pelota as P

class PelotaLetra(P):
    def __init__(self, identificador, participante):
        super().__init__(identificador, participante)
        self.__letra = 'X'
    
    def generarValor(self):
        letras = ["A", "B", "C", "D"]
        self.__color = random.choice(colores)
    
    def pintarPelota(self):
        colores = ["azul", "verde", "rojo"]
        self.__color = random.choice(colores)
    
    def __str__(self):
        letra = str(self.__letra)
        return f"{super().__str__()}\nLetra: {letra}"
