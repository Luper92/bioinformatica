import os
import time
import random

class Game:
    initialADN = ""
    arnm = ""
    arnt = ""


    arn = {
    "chain": ["AUG","UAA", "UGA", "UAG","UUU","UUC","AAU", "UUG", "CUU", "CUC","UGU", "UGC", "GAU", "GAC", "GAA", "GAG", "GUU", "GUC", "GUA", "GUG",
    "GGU", "GGC", "GGA", "GGG","UCU", "UCC", "UCA", "UCG", "CCU", "CCC", "CCA", "CCG",
    "ACU", "ACC", "ACA", "ACG","UAU", "UAC","CAU", "CAC","GAU", "GAC","GAA", "GAG","AAA", "AAG",
    "UGG","CGU", "CGC", "CGA", "CGG","AGA", "AGG","AGU", "AGC",
    "AUU", "AUC","GCA", "GCG","CUU", "CUC", "CUA", "CUG", "UUA", "UUG",
    "AUG","AAU", "AAC","CAA", "CAG"]
    }

    adn = {
    "chain": ["ATG","TAA", "TGA", "TAG","TTT","TTC","AAT", "TTG", "CTT", "CTC", "CTA", "CTG","TGT", "TGC", "GAT", "GAC", "GAA", "GAG", "GTT", "GTC", "GTA", "GTG",
    "GGT", "GGC", "GGA", "GGG","TCT", "TCC", "TCA", "TCG", "CCT", "CCC", "CCA", "CCG",
    "ACT", "ACC", "ACA", "ACG","TAT", "TAC","CAT", "CAC","GAT", "GAC","GAA", "GAG","AAA", "AAG",
    "TGG","CGT", "CGC", "CGA", "CGG","AGA", "AGG","AGT", "AGC",
    "ATT", "ATC","GCA", "GCG","CTT", "CTC", "CTA", "CTG", "TTA", "TTG",
    "ATG","AAT", "AAC","CAA", "CAG"]
    }



    def getRandomChain(self):
        number = len(self.adn["chain"])
        rand = random.randrange(0, number-1)
        return self.adn["chain"][(rand)]

    def createADNChainWith(self, number):
        chain = self.adn
        returnChain = {"chain":[]}
        i=0
        while(i<number):
            codon = self.getRandomChain()

            #chain = chain + codon

            returnChain["chain"].append(codon)
            #oldARNList.append(codon)
            #chain.update({"chain": oldARNList})
            #print(chain)

            i+=1
        return returnChain

    def chainToPrint(self, chain):
        copyChain = chain["chain"] #ojo, chain es un diccionario con "chain":[....]
        index = 0
        returnChain = ""
        while(index < len(copyChain)-1):
            returnChain +=copyChain[index]
            returnChain = returnChain + " - "
            index += 1
        if(len(copyChain)>0):
            returnChain +=copyChain[index]
        return returnChain

    def getARNNucleotidFor(self, n):
        if(n == "A"):
            return "U"
        elif(n == "G"):
            return "C"
        elif(n == "T"):
            return "A"
        else: return "G"

    def getARNTNucleotidFor(self, n):
        if (n == "A"):
            return "U"
        elif (n == "G"):
            return "C"
        elif (n == "U"):
            return "A"
        else:
            return "G"

    def transcript(self, string):
        returnNucleotids = ""
        returnNucleotids += self.getARNNucleotidFor(string[0])
        returnNucleotids += self.getARNNucleotidFor(string[1])
        returnNucleotids += self.getARNNucleotidFor(string[2])
        return returnNucleotids

    def transcriptARNt(self, string):
        returnNucleotids = ""
        returnNucleotids += self.getARNTNucleotidFor(string[0])
        returnNucleotids += self.getARNTNucleotidFor(string[1])
        returnNucleotids += self.getARNTNucleotidFor(string[2])
        return returnNucleotids

    def createARNChainWith(self, chain):
        arnChain = {"chain":[]}
        for elem in chain["chain"]:
            arnChain["chain"].append(self.transcript(elem))
        return arnChain

    def transcript(self, string):
        returnNucleotids = ""
        returnNucleotids += self.getARNNucleotidFor(string[0])
        returnNucleotids += self.getARNNucleotidFor(string[1])
        returnNucleotids += self.getARNNucleotidFor(string[2])
        return returnNucleotids

    def createARNtChainWith(self, chain):
        arnChain = {"chain":[]}
        for elem in chain["chain"]:
            arnChain["chain"].append(self.transcriptARNt(elem))
        return arnChain

    def getCorrectARN(self, tempARNChain):
        return tempARNChain["chain"].pop(0)

    def getCorrectARNt(self, tempARNChain):
        return tempARNChain["chain"].pop(0)



class GameOptions:
    option1 = "una opcion"
    option2 = "otra opcion"
    option3 = "otra otra opcion"
    correct = ""
    correctNumber = 0
    score = 10

    def setOptions(self, arnChain, correct):
        self.correct = correct
        listCopy = arnChain["chain"]
        #quitar respuesta correcta
        try:
            listCopy.remove(correct)
        except:
            None

        number = len(listCopy)
        rand = random.randrange(0, number - 1)
        self.option1 = listCopy[rand]
        listCopy.pop(rand)

        number = len(listCopy)
        rand = random.randrange(0, number - 1)
        self.option2 = listCopy[rand]
        listCopy.pop(rand)

        number = len(listCopy)
        rand = random.randrange(0, number - 1)
        self.option3 = listCopy[rand]
        listCopy.pop(rand)


        rand2 = random.randrange(1, 4)
        #print("result de rand2 :" + str(rand2))
        if(rand2 == 3):
            self.option3 = correct
            self.correctNumber = 3
        elif(rand2 == 2):
            self.option2 = correct
            self.correctNumber = 2
        else:
            self.option1 = correct
            self.correctNumber = 1



#n = createChainWith(10)
#print(n)
#print(createARNChainWith(n))

#c = chainToPrint(n)
#print(c)

#opt = Game()
#n = {"chain":["algo"]}
#print(opt.getCorrectARN(n))
#print(len(n.get("chain")))


#opt = GameOptions()
#opt.setOptions("AAA")
#print(str(opt.option1))
#print(str(opt.option2))
#print(str(opt.option3))




##class ChainCreator:
##dna_chain = ""
## def __init__():

