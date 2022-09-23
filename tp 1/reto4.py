# coding=utf-8

# RETO IV: ¿Cadenas?¿letras? Si hablamos de cadenas y letras en Biología,
#lo primero que se nos viene a la cabeza son las macromoléculas. Como bien sabemos,
#el ADN es un mensaje en clave que guía la síntesis de proteínas. Este mensaje está escrito por
#una secuencia determinada de 4 nucleótidos distintos representados por las letras A, T, G y C.
#El contenido de C y G (es decir el porcentaje de CG) presente en el ADN de un organismo es una característica
#distintiva: por ejemplo las Actinobacterias tienen un contenido característicamente más alto de CG que otros organismos.
#Ahora, contar la cantidad de C y G en una cadena de ADN larguísima a mano puede ser un verdadero tedio ¿Podrías crear un
#programa que calcule el porcentaje de C y G de una cadena dada de ADN? ¡Compartinos tu código en nuestro grupo de Facebook
#‘Talleres de programación Orientada a la Biologia - SBG_UNQ’!Buscanos en Twitter!

DNAChain = 'TGATAAGAGTACCCAGAATAAAATGAATAACTTTTTAAAGACAAAATCCTCTGTTATAATATTGCTAAAATTATTCAGAGTAATATTGTGGATTAAAGCCACAATAAGATTTATAATCTTAAATGATGGGACTACCATCCTTACTCTCTCCATTTCAAGGCTGACGATAAGGAGACCTGCTTTGCCGAGGAGGTACTACAGTTCTCTTCACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTTTTAATATGTCCAGTATTCATTTTTGCATGTTTGGTTAGGCTAGGGCTTAGGGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTAGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTCTATTGTGCCATACTGTTGAATGTTTATAATGCATGTTCTGTTTCCAAATTTCATGAAATCAAAACATTAATTTATTTAAACATTTACTTGAAATGTTCACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTTTTAATATGTCCAGTATTCATTTTTGCATGTTTGGTTAGGCTAGGGCTTAGGGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTAGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTCTATTGTGCCATACTGTTGAATGTTTATAATGCATGTTCTGTTTCCAAATTTCATGAAATCAAAACATTAATTTATTTAAACATTTACTTGAAATGTGGTGGTTTGTGATTTAGTTGATTTTATAGGCTAGTGGGAGAATTTACATTCAAATGTCTAAATCACTTAAAATTTCCCTTTATGGCCTGACAGTAACTTTTTTTTATTCATTTGGGGACAACTATGTCCGTGAGCTTCCATCCAGAGATTATAGTAGTAAATTGTAATTAAAGGATATGATGCACGTGAAATCACTTTGCAATCAT'

countC = DNAChain.count('C')
countG = DNAChain.count('G')
totalCG = DNAChain.count('CG')

lengthDNA = len(DNAChain)
print('Cadena a trabajar: ' + DNAChain)

print('Porcentaje de C: ' + str(countC*100/lengthDNA))
print('Porcentaje de G: ' + str(countG*100/lengthDNA))
print('Porcentaje de CG(total): ' + str(totalCG*100/lengthDNA))