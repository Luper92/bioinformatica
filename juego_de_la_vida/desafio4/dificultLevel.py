from chainMethods import *


class DificultLevel:
    game = None
    questionValue = 0
    bonusMaxValue = 0
    currentBonusValue = 0

    def __init__(self, gameOfLife):
        self.game = gameOfLife

    def decreasedScorePerTime(self, game):
        # initial score = 300
        # for each 20 seconds = score-10
        # so at 900 sec, score-300 and stops decrease
        # so at 900 sec, score-300 and stops decrease
        # 360 sec = 6 min

        timeNegScore = game.tiempoTotal / 30 * 10
        if (timeNegScore > 300):
            return 300
        else:
            return (int(timeNegScore))


    def start(self, game):
        return 0
    
    def start2(self, game):
        game.arnChainInPlay = game.completeARNChain

    def endBonus(self, game):
        return 0

    def explain(self):
        return 0

    def correctAnswer(self, game):
        game.customPrint("Respuesta Correcta!")
        game.correctAnswers += 1
        p = game.score + self.questionValue
        game.customPrint("Puntaje actual: " + str(p) + " ( " + str(game.score) + " + " + str(self.questionValue) + " )")
        game.score += self.questionValue

    def wrongAnswer(self, game):
        game.customPrint("incorrecto! El codon era: " + game.currentGameOption.correct + ". Siguiente:")

    def correctBonusAnswer(self, game):
        game.customPrint("Respuesta Correcta!")
        self.currentBonusValue += 1

    def wrongBonusAnswer(self, game):
        game.customPrint("incorrecto! El codon era: " + game.currentGameOption.correct + ". Siguiente:")




    def continueTurn(self):
        return 0

    def endGame1(self):
        return 0

    def bonusLevel(self, game):
        return 0


class Easy(DificultLevel):

    def __init__(self, gameOfLife):
        super
        self.questionValue = 0
        gameOfLife.initScorePerTime = 0
        gameOfLife.scorePerTimeElapsed = 0
        self.bonusMaxValue = 0

    def decreasedScorePerTime(self, game):
        return 0

    def endGame1(self, game):
        game.detenerCronometro()

        p = game.showStatics()
        if(p > 99):
            game.customPrint('-----PERFECTO!! Estas mas que listo para el siguiente nivel!-----')
        elif(p > 50):
                game.customPrint('-----MUY BIEN!! Ya estas listo para el siguiente nivel-----')
        elif(p > 25):
            game.customPrint('-----Bueno, algunos tropezones por el camino. Hay que seguir intentando-----')
        else:
            game.customPrint('...')
            game.customPrint('¿Siquiera lo estabas intentando?')


    def explain(self, game):
        game.customPrint("Para este tutorial te daremos una cadena corta de solo 4 codones")
        game.customPrint("y un 'machete' para que puedas calcular las cadenas resultantes esperadas")
        game.customPrint("Sin embargo no recibirás ningun puntaje.")
        game.customPrint("Comencemos!")
        
    def explain2(self, game):
        return 0


    def continueTurn2(self, game):
        ## obtener cadena ARN correcto, es decir, el primer trio de nucleotidos de arnChainInPlay para setear opciones
        ##obtener el primer trio de nucleotidos de chainInPlay

        game.correctARN = game.dataGame.getCorrectARNt(game.arntChainInPlay)
        #print("correcto temporal: " + game.correctARN)
        game.currentADN = game.arnChainInPlay["chain"].pop(0)
        game.currentGameOption.setOptions(game.dataGame.arn, game.correctARN)

        ## Ahora a mostrar
        game.customPrint("Machete: \n"
                         'G -> C,'
                         'A -> U,'
                         'C -> G,'
                         'U -> A')

        game.customPrint("¿Cual trio de nucleotidos machea con " + game.currentADN + " ?")

        game.customPrint("1) " + game.currentGameOption.option1)
        game.customPrint("2) " + game.currentGameOption.option2)
        game.customPrint("3) " + game.currentGameOption.option3)

        #print("opcion correcta" + str(game.currentGameOption.correctNumber))
        while True:
            try:
                answer = input("por favor, elige una opcion: ")
                if (int(answer) == game.currentGameOption.correctNumber):
                    self.correctBonusAnswer(game)
                else:
                    self.wrongBonusAnswer(game)
                break
            except:
                print("No, esa no es opcion válida")


    def continueTurn(self, game):
        ## obtener cadena ARN correcto, es decir, el primer trio de nucleotidos de arnChainInPlay para setear opciones
        ##obtener el primer trio de nucleotidos de chainInPlay

        game.correctARN = game.dataGame.getCorrectARN(game.arnChainInPlay)
        #print("correcto temporal: " + game.correctARN)
        game.currentADN = game.chainInPlay["chain"].pop(0)
        game.currentGameOption.setOptions(game.dataGame.arn, game.correctARN)

        ## Ahora a mostrar
        game.customPrint("Machete: \n"
                         'G -> C,'
                         'A -> U,'
                         'C -> G,'
                         'T -> A')

        game.customPrint("¿Cual trio de nucleotidos machea con " + game.currentADN + " ?")

        game.customPrint("1) " + game.currentGameOption.option1)
        game.customPrint("2) " + game.currentGameOption.option2)
        game.customPrint("3) " + game.currentGameOption.option3)

        #print("opcion correcta" + str(game.currentGameOption.correctNumber))
        while True:
            try:
                answer = input("por favor, elige una opcion: ")
                if (int(answer) == game.currentGameOption.correctNumber):
                    self.correctAnswer(game)
                else:
                    self.wrongAnswer(game)
                break
            except:
                print("No, esa no es opcion válida")

        if (game.gameOver1()):
            game.bonusLevel()
            self.endGame1(game)


    def start(self, game):
        game.initScorePerTime = 0
        game.questionValue = 0
        game.chainNumber = 4
        game.turn = game.chainNumber
        self.bonusMaxValue = game.chainNumber

        game.currentGameOption = GameOptions()

        game.chain = game.dataGame.createADNChainWith(game.chainNumber)
        game.chainInPlay = game.chain

        game.completeARNChain = game.dataGame.createARNChainWith(game.chain)
        game.arnChainInPlay = game.dataGame.createARNChainWith(game.chain)




        game.completeARNtChain =  game.dataGame.createARNtChainWith(game.completeARNChain)

        game.arntChainInPlay = game.dataGame.createARNtChainWith(game.completeARNChain)

        #Guardamos las cadenas:
        game.dataGame.initialADN = game.dataGame.chainToPrint(game.chain)
        game.dataGame.arnm = game.dataGame.chainToPrint(game.completeARNChain)
        game.dataGame.arnt = game.dataGame.chainToPrint(game.completeARNtChain)


        game.customPrint("-----INICIO DEL TUTORIAL----- ")

        self.explain(game)

class Normal(DificultLevel):

    def __init__(self, gameOfLife):
        super
        self.questionValue = 20

    def explain(self, game):
        game.customPrint("Deberás analizar una cadena de 6 codones y dar su posible resultado para una transcripcion de ARNm")
        game.customPrint("tendrás 3 opciones por cada codón")
        game.customPrint("Comencemos!")

    def continueTurn(self, game):
        ## obtener cadena ARN correcto, es decir, el primer trio de nucleotidos de arnChainInPlay para setear opciones
        ##obtener el primer trio de nucleotidos de chainInPlay
        game.correctARN = game.dataGame.getCorrectARN(game.arnChainInPlay)
        #print("correcto temporal: " + game.correctARN)
        game.currentADN = game.chainInPlay["chain"].pop(0)
        game.currentGameOption.setOptions(game.dataGame.arn, game.correctARN)

        game.customPrint("¿Cual trio de nucleotidos machea con " + game.currentADN + " ?")

        game.customPrint("1) " + game.currentGameOption.option1)
        game.customPrint("2) " + game.currentGameOption.option2)
        game.customPrint("3) " + game.currentGameOption.option3)

        #print("opcion correcta" + str(game.currentGameOption.correctNumber))

        while True:
            try:
                answer = input("por favor, elige una opcion: ")
                if(int(answer) == game.currentGameOption.correctNumber):
                    self.correctAnswer(game)
                else:
                    self.wrongAnswer(game)
                break
            except:
                print("No, esa no es opcion válida")

        if(game.gameOver1()):
            game.bonusLevel()
            self.endGame1(game)

    def endGame1(self, game):
        game.detenerCronometro()

        p = game.showStatics()
        if(p > 99):
            game.customPrint('-----PUNTAJE PERFECTO!! Estas mas que listo para el siguiente '
                             'nivel!-----')
        elif(p > 50):
            game.customPrint('-----GENIAL!! Ya estas listo para el siguiente nivel-----')
        elif(p > 25):
            game.customPrint('-----Bueno, algunos tropezones por el camino. Hay que seguir intentando-----')
        else:
            game.customPrint('...')
            game.customPrint('mm tal vez deberias volver al tutorial...')

    def continueTurn2(self, game):
        ## obtener cadena ARN correcto, es decir, el primer trio de nucleotidos de arnChainInPlay para setear opciones
        ##obtener el primer trio de nucleotidos de chainInPlay

        game.correctARN = game.dataGame.getCorrectARNt(game.arntChainInPlay)
        #print("correcto temporal: " + game.correctARN)
        game.currentADN = game.arnChainInPlay["chain"].pop(0)
        game.currentGameOption.setOptions(game.dataGame.arn, game.correctARN)

        game.customPrint("¿Cual trio de nucleotidos machea con " + game.currentADN + " ?")

        game.customPrint("1) " + game.currentGameOption.option1)
        game.customPrint("2) " + game.currentGameOption.option2)
        game.customPrint("3) " + game.currentGameOption.option3)

        #print("opcion correcta" + str(game.currentGameOption.correctNumber))
        while True:
            try:
                answer = input("por favor, elige una opcion: ")
                if (int(answer) == game.currentGameOption.correctNumber):
                    self.correctBonusAnswer(game)
                else:
                    self.wrongBonusAnswer(game)
                break
            except:
                print("No, esa no es opcion válida")


    def start(self, game):

        game.chainNumber = 6
        game.turn = 6
        self.bonusMaxValue = game.chainNumber


        game.currentGameOption = GameOptions()

        game.chain = game.dataGame.createADNChainWith(game.chainNumber)
        game.chainInPlay = game.chain

        game.completeARNChain = game.dataGame.createARNChainWith(game.chain)
        game.arnChainInPlay = game.dataGame.createARNChainWith(game.chain)

        game.completeARNtChain =  game.dataGame.createARNtChainWith(game.completeARNChain)

        game.arntChainInPlay = game.dataGame.createARNtChainWith(game.completeARNChain)

        # Guardamos las cadenas:
        game.dataGame.initialADN = game.dataGame.chainToPrint(game.chain)
        game.dataGame.arnm = game.dataGame.chainToPrint(game.completeARNChain)
        game.dataGame.arnt = game.dataGame.chainToPrint(game.completeARNtChain)

        self.explain(game)

class Hard(DificultLevel):

    def __init__(self, gameOfLife):
        super
        self.questionValue = 30

    def explain(self, game):
        game.customPrint(
            "Deberás analizar una cadena de 6 codones y dar su posible resultado para una transcripcion de ARNm")
        game.customPrint("Por cada codon deberás tipear su posible resultado")
        game.customPrint("Comencemos!")

    def endGame1(self, game):
        game.detenerCronometro()

        p = game.showStatics()
        if (p > 99):
            game.customPrint('-----ERES ASOMBROSOO!!-----')
        elif (p > 50):
            game.customPrint('-----MUY BIEN!!-----')
        elif (p > 25):
            game.customPrint('-----Al menos asumiste un gran riesgo. Prueba de nuevo-----')
        else:
            game.customPrint('jeje, tal vez aun no estes listo para este nivel')



    def continueTurn(self, game):
        ## obtener cadena ARN correcto, es decir, el primer trio de nucleotidos de arnChainInPlay para setear opciones
        ##obtener el primer trio de nucleotidos de chainInPlay
        correctARN = game.dataGame.getCorrectARN(game.arnChainInPlay)
        #print("correcto temporal: " + correctARN)
        currentADN = game.chainInPlay["chain"].pop(0)
        game.currentGameOption.setOptions(game.dataGame.arn, correctARN)

        ## Ahora a mostrar
        game.customPrint("¿Que nucleotidos machean con " + str(currentADN) + " ?")

        # self.customPrint("1) " + self.currentGameOption.option1)
        # self.customPrint("2) " + self.currentGameOption.option2)
        # self.customPrint("3) " + self.currentGameOption.option3)

        while True:
            try:
                answer = input("por favor, escribe el trio de nucleotidos que machea: ")
                if(answer.upper() == game.currentGameOption.correct.upper()):
                    self.correctAnswer(game)
                else:
                    self.wrongAnswer(game)
                break
            except:
                print("No, esa no es opcion válida")

        if(game.gameOver1()):
            game.bonusLevel()
            self.endGame1(game)

    def continueTurn2(self, game):
        ## obtener cadena ARN correcto, es decir, el primer trio de nucleotidos de arnChainInPlay para setear opciones
        ##obtener el primer trio de nucleotidos de chainInPlay

        game.correctARN = game.dataGame.getCorrectARNt(game.arntChainInPlay)
        #print("correcto temporal: " + game.correctARN)
        game.currentADN = game.arnChainInPlay["chain"].pop(0)
        game.currentGameOption.setOptions(game.dataGame.arn, game.correctARN)

        ## Ahora a mostrar
        game.customPrint("¿Que nucleotidos machean con " + game.currentADN + " ?")

        # self.customPrint("1) " + self.currentGameOption.option1)
        # self.customPrint("2) " + self.currentGameOption.option2)
        # self.customPrint("3) " + self.currentGameOption.option3)

        while True:
            try:
                answer = input("por favor, escribe el trio de nucleotidos que machean con: ")
                if (answer.upper() == game.currentGameOption.correct.upper()):
                    self.correctBonusAnswer(game)
                else:
                    self.wrongBonusAnswer(game)
                break
            except:
                print("No, esa no es opcion válida")


    def start(self, game):
        game.chainNumber = 6
        game.turn = 6
        self.bonusMaxValue = game.chainNumber

        game.currentGameOption = GameOptions()

        game.chain = game.dataGame.createADNChainWith(game.chainNumber)
        game.chainInPlay = game.chain

        game.completeARNChain = game.dataGame.createARNChainWith(game.chain)
        game.arnChainInPlay = game.dataGame.createARNChainWith(game.chain)

        game.completeARNtChain = game.dataGame.createARNtChainWith(game.completeARNChain)

        game.arntChainInPlay = game.dataGame.createARNtChainWith(game.completeARNChain)

        # Guardamos las cadenas:
        game.dataGame.initialADN = game.dataGame.chainToPrint(game.chain)
        game.dataGame.arnm = game.dataGame.chainToPrint(game.completeARNChain)
        game.dataGame.arnt = game.dataGame.chainToPrint(game.completeARNtChain)

        self.explain(game)
