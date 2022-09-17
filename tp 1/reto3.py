# coding=utf-8
# RETO III: Digamos que el ADN no es más que un mensaje en clave, que debe ser descifrado o interpretado para
# la síntesis de proteínas. El mensaje está escrito por una secuencia determinada de 4 nucleótidos distintos
# representados por las letras A, T, G y C. Dentro de la célula, el mensaje es transportado por otra
# molécula, el ARN, muy similar al ADN pero con U en vez de T. En este mensaje, cada triplete o grupo de tres
# letras del ARN se denomina codón, y cada aminoácido de las proteínas está codificado por uno o varios codones.
# Así por ejemplo el codón ‘AUG’ codifica para el aminoácido Metionina , el codón ‘AAA’ para Lisina, el codón ‘CUA’
# para Leucina, etc. ¿Podrías escribir una cadena de ARN que codifique para el péptido (una cadena corta de aminoácidos)
# ‘Met-Lis-Lis-Lis-Leu-Leu-Met’ combinando las variables met = ‘AUG’, lis = ‘AAA’ y leu = ‘CUA’ utilizando operadores matemáticos?

met = 'AUG'
lis = 'AAA'
leu = 'CUA'
chain = met + lis + lis + lis + leu + leu + met + met

print(chain)