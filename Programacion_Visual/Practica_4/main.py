from PelotaNumero import PelotaNumero as PN
from PelotaLetra import PelotaLetra as PL


def decifrarPremio(pelotaNumero, pelotaLetra):
    vigencia = pelotaNumero.numero
    valor = {"Amarillo": "$1000", "Morado": "$2000", "Rosa": "$3000"}.get(pelotaNumero.color)
    unidad = {"Azul":"Xochimilco", "Verde":"Iztapalapa", "Rojo":"Azcapotzalco"}.get(pelotaLetra.color)
    categoria = {"A": "Libros físicos", "B": "Libros electrónicos", "C": "Papelería", "D": "Souvenirs"}.pelotaLetra.letra

def main():
    