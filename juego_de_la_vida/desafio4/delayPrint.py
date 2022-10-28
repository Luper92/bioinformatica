import time
import sys

class DelayPrint:

    def delay_print(self, s):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.02)

    def delay_print2(self, string):
        for char in string:
            print(char, end='')
            time.sleep(.03)
        time.sleep(1)

    def delay_print3(self, s):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.2)

    def showDialogue(self, string):
        self.delay_print2(string + '\n')

    def showScore(self, string, string2):
        self.delay_print2(string)
        time.sleep(2)
        print(string2 + '\n')

    def printTitle(self):
        n1 = "                      ┏━━━━•❅•°•❈•°•❅•°•❈•°•❅•°•❈•°•❅•━━━━┓"
        n2 = "                      ❍......................................❍"
        n3 = "                      ❍.........EL JUEGO DE LA VIDA..........❍"
        n4 = "                      ❍......................................❍"
        n5 = "                      ┗━━━━•❅•°•❈•°•❅•°•❈•°•❅•°•❈•°•❅•━━━━┛"

        self.showInstantDialogue(n1)
        self.showInstantDialogue(n2)
        self.showInstantDialogue(n3)
        self.showInstantDialogue(n4)
        self.showInstantDialogue(n5)

    def printStart(self):
        self.delay_print2("Despiertas en un gran cuarto cerrado con varias instalaciones y frascos de diferentes tamaños\n")
        self.delay_print2("Una voz electrónica te habla desde una gran pantalla\n")

    def showInstantDialogue(self, msg):
        print(msg)
        time.sleep(.5)

    def printSpace(self):
        print("------------------------------------------")

    def printStatics(self, string1, string2):
        self.delay_print(string1)
        time.sleep(.5)
        self.showInstantDialogue(string2)



n6 = "BIP Necesitas un usuario para usar las instalaciones BIP"

n7 = "Bienvenide persona x a nuestro laboratorio secreto subterraneo" \
     "lamentablemente no puedo dejarte ir sin que me demuestres tus conocimientos respecto a la producción de proteínas que comienzan" \
     "desde el centro del núcleo de una celula eucariota."\
     "Cual crees sería el nivel adecuado para evaluarte? "\
     "tutorial"\
     "Deseas leer el manual?"\
     "Para ser más especificos, analizaremos una cadena" \
     "de adn y construiremos juntos, de manera sencilla, una cadena de aminoacidos que compondrán una proteina."








#delay_print2("Hola, este es un print de prueba, espero se vea bien jeje", "y un puntaje")