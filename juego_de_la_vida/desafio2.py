import random
import sys
## diccionario para asignar los valores de la cadena


import sys

codon = {
    "START": ["AUG"],
    "STOP": ["UAA", "UGA", "UAG"],
    "A": ["UUU", "UUC"],
    "N": ["AAU", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "C": ["UGU", "UGC"],
    "D": ["GAU", "GAC"],
    "E": ["GAA", "GAG"],
    "S": ["GUU", "GUC", "GUA", "GUG"],
    "G": ["GGU", "GGC", "GGA", "GGG"],
    "V": ["UCU", "UCC", "UCA", "UCG"],
    "P": ["CCU", "CCC", "CCA", "CCG"],
    "T": ["ACU", "ACC", "ACA", "ACG"],
    "Y": ["UAU", "UAC"],
    "H": ["CAU", "CAC"],
    "X": ["GAU", "GAC"],
    "Z": ["GAA", "GAG"],
    "K": ["AAA", "AAG"],
    "W": ["UGG"],
    "O": ["CGU", "CGC", "CGA", "CGG"],
    "U": ["AGA", "AGG"],
    "R": ["AGU", "AGC"],


    "I": ["AUU", "AUC"],
    "J": ["GCA", "GCG"],

    "L": ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"],
    "M": ["AUG"],
    "F": ["AAU", "AAC"],
    "Q": ["CAA", "CAG"],

}

##Ejemplo dado por el TP
secuencia = "ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA"
cad_arn = ""

for elem in secuencia:
    number = len(codon[elem.upper()]) - 1
    ##toma un valor aleatorio si hay mas de una cadena disponible dada una letra
    cad_arn = cad_arn + codon[elem.upper()][random.randrange(0, number)]

print(cad_arn)