from datetime import *
from dificultLevel import *
from delayPrint import *

import os
import time
import random
from warnings import catch_warnings

from chainMethods import *

class GameOfLife:

    hora_inicio = 0
    hora_final = 0
    tiempoTotal = 0
    tiempoTotalPrint = 0
    deathTime = 0.0
    deathTimeDef = 0.0
    initScorePerTime = 300
    scorePerTimeElapsed = 0
    finalScore = 0

    dificultLevel = ""
    askedDificult = False
    correctAnswers = 0

    dataGame = Game()
    questionValue = 10

    name = ""
    chainNumber = 10  # 10 codones para analizar, como para empezar
    turn = 10
    chain = None
    score = 0


    #chain = dataGame.createADNChainWith(chainNumber)
    #arntChain = dataGame.createARNChainWith(chain)

    #chainInPlay = chain

    #arntChain = dataGame.createARNChainWith(chain)

    #completeARNChain = dataGame.createARNChainWith(chain)
    #arnChainInPlay = completeARNChain

    currentGameOption = GameOptions()
    chainInPlay = None
    completeARNtChain = None
    completeARNChain = None
    arnChainInPlay = None
    arntChainInPlay = None

    currentARN = ""
    currentADN = ""

    delayPrint = DelayPrint()

    def printSpace(self):
        self.delayPrint.printSpace()

    def showDialogue(self, msg):
        self.delayPrint.showDialogue(msg)

    def showInstantDialogue(self, msg):
        self.delayPrint.showInstantDialogue(msg)

    def customPrint(self, message: object) -> object:
        time.sleep(1)
        self.deathTime += 1
        print(message)

    def printStatics(self, str1, str2):
        self.delayPrint.printStatics(str1, str2)


    def customInput(self, message):
        myInput = input(message)
        if(myInput == "SALIR"):
            raise Exception()
        #time.sleep(1.5)
        #self.deathTime += 1.5
        return myInput

    def decreasedScorePerTime(self):
        self.dificultLevel.decreasedScorePerTime(self)

    def segundos_a_segundos_minutos_y_horas(self, segs):
        horas = int(segs / 60 / 60)
        segs -= horas * 60 * 60
        minutos = int(segs / 60)
        segs -= minutos * 60
        t= f"{horas:02d}:{minutos:02d}:{segs:02d}"
        #print(t)
        return t

    def detenerCronometro(self):
        self.hora_final = datetime.now()
        self.deathTimeDef = self.deathTime
        t = (self.hora_final - self.hora_inicio)
        segundos_transcurridos = t.total_seconds()
        n = int(segundos_transcurridos)
        n -= int(self.deathTimeDef)
        self.tiempoTotal = n
        self.tiempoTotalPrint = self.segundos_a_segundos_minutos_y_horas(n)

    def bonusLevel(self):
        self.customPrint("----------NIVEL BONUS----------")
        self.showDialogue("ya formamos el ARNm resultante, ahora nos toca predecir el ARNt para formar asi la proteina")

        self.showDialogue('Nuestra cadena ARNm:')
        self.showDialogue(self.dataGame.chainToPrint(self.completeARNChain))

        self.customPrint(' Comencemos!')

        self.dificultLevel.start2(self)

        n = self.turn
        while (n > 0):
            self.avanzarTurno2()
            n = n - 1

        self.dificultLevel.endBonus(self)


    def explicarReglas(self):

        self.showDialogue("Cada base de una cadena especifica se codifica de la siguiente manera:")
        self.showInstantDialogue("ADN        =>    ARNm ")
        self.showInstantDialogue("T (Timina) => A (Adenina) ")
        self.showInstantDialogue("G (Glicina) => C( Citocina) ")
        self.showInstantDialogue("C (Citocina) => G (Glicina) ")
        self.showInstantDialogue("A (Adenina) => U (Urácilo) \n"
                                 "")

        self.showInstantDialogue("ARNm        =>    ARNt ")
        self.showInstantDialogue("U (Urácilo) <=> A (Adenina) ")
        self.showInstantDialogue("G (Glicina) <=> C (Citocina) ")
        self.showInstantDialogue("C (Citocina) => G (Glicina) ")
        self.showInstantDialogue("A (Citocina) => U (Urácilo) \n")

        self.showDialogue("Las cadenas reales son mucho mas complejas y largas que las vistas en esta simulación.")
        self.showDialogue("Puedes probar el Tutorial si aun no estas familiarizado en el tema\n")
        self.printSpace()

    def increaseDificult(self):
        self.questionValue = 20
        self.dificultLevel += 1

    def gameOver1(self):
        return len(self.chainInPlay["chain"]) < 1

    def showStatics(self):
        self.customPrint('-----------FIN DE PARTIDA--------------')
        self.customPrint('-------ESTADISTICAS DE ' + str(self.name) + '-------')

        porcentaje = int(self.correctAnswers * 100 / self.chainNumber)
        negScorePerTime = int(self.dificultLevel.decreasedScorePerTime(self))

        self.printStatics('TIEMPO ENTRE RESPUESTAS:', str(self.tiempoTotalPrint))

        self.printStatics('PUNTUACION POR RESPUESTAS: +', str(self.score))

        self.printStatics('PUNTUACION INICIAL POR TIEMPO: +', str(self.initScorePerTime))

        self.printStatics('PENALIDAD POR TIEMPO TRANSCURRIDO: -', str(negScorePerTime))

        ptotal = int(self.score + self.initScorePerTime - negScorePerTime)
        self.printStatics('PUNTUACION TOTAL: ', str(ptotal))

        self.printStatics('ACIERTOS: ', str(self.correctAnswers) + '/' + str(self.chainNumber) + " (" + str(int(porcentaje)) + "%)")

        porcentajeBonus = int(self.dificultLevel.currentBonusValue * 100 / self.dificultLevel.bonusMaxValue)

        self.customPrint('-------NIVEL BONUS--------')

        self.printStatics('ACIERTOS: ',str(self.dificultLevel.currentBonusValue) + '/' + str(self.dificultLevel.bonusMaxValue) + " (" + str(int(porcentajeBonus)) + "%)")

        valorBonus = int(ptotal * porcentajeBonus / 100)

        self.printStatics('VALOR DE BONUS: +',str(valorBonus))

        porcentajeTotal = int((porcentaje + porcentajeBonus) / 2)

        self.customPrint('----------------------------')

        self.printStatics('CADENA DE ADN Inicial:     ', self.dataGame.initialADN)
        self.printStatics('CADENA DE ARNm resultante: ', self.dataGame.arnm)
        self.printStatics('CADENA DE ARNt final:      ', self.dataGame.arnt)

        self.printStatics('PUNTAJE FINAL: ', str(int(ptotal + valorBonus)))

        self.printStatics('PORCENTAJE FINAL: ', str(int(porcentajeTotal)) + "%")

        return porcentajeTotal

    def avanzarTurno(self):
        self.dificultLevel.continueTurn(self)

    def avanzarTurno2(self):
        self.dificultLevel.continueTurn2(self)


    def clearConsole(self):
        return os.system('clear')


    def stepTwo(self):

        self.customPrint(f' Muy bien {self.name} , Ya podemos comenzar!!!')

        self.showDialogue('Ahora tratemos de crear una cadena ARNm a partir de la siguiente cadena')
        time.sleep(1)
        self.showDialogue(self.dataGame.chainToPrint(self.chain))



        self.customPrint('-----------------COMIENZO DE PARTIDA-------------------')

        #Hora actual
        self.hora_inicio = datetime.now()
        self.deathTime = 0.0
        self.printSpace()

        n = self.turn
        while(n > 0):

            self.avanzarTurno()
            n = n - 1
            self.printSpace()

    def stepOne(self):
        self.showDialogue("IA:-Selecciona una opcion para empezar. Recomiendo el 3, es el que mas me gusta je je je")
        self.showInstantDialogue("1) Tutorial")
        self.showInstantDialogue("2) Normal")
        self.showInstantDialogue("3) Dificil")

        while True:
            try:
                answer = input("por favor, escoje un nivel: ")
                if (int(answer) == 1):
                    self.dificultLevel = Easy(self)
                elif(int(answer) == 2):
                    self.dificultLevel = Normal(self)
                elif(int(answer) == 3):
                    self.dificultLevel = Hard(self)
                else:
                    raise Exception
                break
            except:
                print("Por favor, escoge una opción válida")
        self.dificultLevel.start(self)

        self.stepTwo()



    def stepThree(self):
        return 0

    def iniciar(self):

        self.delayPrint.printTitle()
        #self.customPrint('-------------------EL JUEGO DE LA VIDA----------------------')
        self.customPrint(' ')
        self.delayPrint.printStart()

        self.name = self.customInput('"*BIP* Necesitas un usuario para usar las instalaciones *BIP*". :\n> ')
        self.showDialogue(' Bienvenide ' + str(self.name) + ' al laboratorio secreto subterraneo de la UNQ sede Bernal. \n')
        self.showDialogue('Soy AI, una IA programada para cuidar este lugar.\n')
        self.showDialogue('Para ser libre deberas demostrarme que tanto sabes sobre el proceso de creacion de proteinas desde el nucleo de una celula eucariota\n')
        self.showDialogue('o deberé destruirt-*BZZZT* ')
        self.showDialogue("-retenerte")

        self.printSpace()

        while True:
            try:
                explicacion = input("Deseas consultar la guía primero? Y/N")
                if(explicacion.upper()=="Y"):
                    self.explicarReglas()
                elif(explicacion.upper()=="N"):
                    break
                else:
                    raise Exception
                break
            except:
                print("Por favor, teclea una opción válida")
        self.stepOne()

# stepOne()
# customPrint(' ')
# stepTwo()
#  customPrint(' ')
#   showScore()
# except:
# customPrint('')

d = GameOfLife()
d.iniciar()