# coding=utf-8
from itertools import combinations


# RETO VII: Ya que encontramos el espécimen de rana con pelo en marte, nos gustaría contrastar
# sus características con las ranas terrestres. Sabiendo que el gen de la proteína diminuta es
# ‘ATGGAAGTTGGAATCCAAGTTGGA’ y el gen de una proteína similar de rana terrestre es
# ‘ATGGAAGTTAATGGAAGTTGGAGGAGA’ ¿podés crear un programa que compare la longitud de
# ambos genes y según cuál sea más grande nos imprima un mensaje informándonos el resultado?


def compararGenes(gen1, gen2):
    if len(gen1) > len(gen2):
        print("El primer gen dado es mas largo")
    else:
        print("El segundo gen dado es mas largo")


if __name__ == '__main__':
genTerrestre = "ATGGAAGTTAATGGAAGTTGGAGGAGA"
genMarciano = "ATGGAAGTTGGAATCCAAGTTGGA"

compararGenes(genTerrestre, genMarciano)
