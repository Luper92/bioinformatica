# coding=utf-8
#RETO V: La Asombrosa Maravillosa es nuestra valiente superheroína. Sus poderes son producto de mutaciones en un gen muy común,
#cuya secuencia en la mayoría de las personas es 'ATGGAACTTGCAATCGAAGTTGGC'. A diferencia de nosotros, el gen mutado de la
#Asombrosa Maravillosa incluye la secuencia 'GTTTGTGGTTG' en su interior. La Asombrosa Maravillosa adquirió sus poderes al
#beber Jugo Vencido. El primer sorbo de esta poción prohibida causa el cambio de todas las citosinas (C) por timinas (T).
#El siguiente sorbo cambia todas las adeninas (A) por guaninas (G). El tercer sorbo cambia las citosinas (C) por adeninas (A).
#El cuarto sorbo... puede ser mortal. ¿Podés escribir un programa que nos diga cuántos sorbos de Jugo Vencido debe beber un portador
#del gen normal, para ganar los poderes de la Asombrosa Maravillosa? ¡Compartinos tu código en nuestro grupo de Facebook ‘Talleres
#de programación Orientada a la Biologia - SBG_UNQ’! Buscanos en Twitter!

def cantidadDeSorbos(cadena):
    sorbos = 0
    genMod = cadena
    if(genMod.count('C')>1):
        sorbos = sorbos+1
        genMod = genMod.replace('C', 'T')
        if(genMod.count('A')>1):
            genMod = genMod.replace('A', 'G')
            sorbos = sorbos + 1
            if (genMod.count('C') > 1): #absurdo pero el tp lo pide.
                genMod = genMod.replace('C', 'A')
                sorbos = sorbos + 1

    print("cantidad de sorbos a tomar: " + str(sorbos))
    print("cadena original: " + cadena)
    print("cadena resultante de tomar los sorbos: " + genMod)

if __name__ == '__main__':
    cadena = 'ATGGAACTTGCAATCGAAGTTGGC'
    cantidadDeSorbos(cadena)