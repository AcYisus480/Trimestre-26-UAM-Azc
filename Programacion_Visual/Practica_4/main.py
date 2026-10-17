import sys
from PelotaLetra import PelotaLetra
from PelotaNumero import PelotaNumero


def leer_archivo():
    participantes = []

    try:
        with open("participantes.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip():
                    identificador, participante = linea.strip().split(",")
                    participantes.append(
                        (identificador.strip(), participante.strip())
                    )
    except FileNotFoundError:
        print("Error: El archivo no existe.\nProceso terminado")
        sys.exit(1)

    return participantes


def decifrarPremio(pelota_numero, pelota_letra):
    valores = {"Amarillo": "$1000", "Morado": "$2000", "Rosa": "$3000"}
    unidades = {
        "Azul": "Xochimilco",
        "Verde": "Iztapalapa",
        "Rojo": "Azcapotzalco",
    }
    categorias = {
        "A": "Libros físicos",
        "B": "Libros electrónicos",
        "C": "Papelería",
        "D": "Souvenirs",
    }

    valor = valores.get(pelota_numero.color)
    unidad = unidades.get(pelota_letra.color)
    categoria = categorias.get(pelota_letra.letra)
    resultado = f"""Identificador: {pelota_letra.identificador}\tParticipante: {pelota_letra.participante}
    Unidad: {unidad}
    Categoria: {categoria}
    Cantidad: {valor}
    Vigencia {pelota_numero.numero} meses\n"""

    with open("premios.txt", "a+", encoding="utf-8") as archivo:
        archivo.write(resultado)


def realizar_sorteo(identificador, participante):
    pelota_letra = PelotaLetra(identificador, participante)
    pelota_numero = PelotaNumero(identificador, participante)

    pelota_letra.generarValor()
    pelota_letra.pintarPelota()
    pelota_numero.generarValor()
    pelota_numero.pintarPelota()

    decifrarPremio(pelota_numero, pelota_letra)
    print(pelota_letra)
    print(pelota_numero)


def main():
    for identificador, participante in leer_archivo():
        realizar_sorteo(int(identificador), participante)

    print("\n--------Proceso terminado--------")


if __name__ == "__main__":
    main()