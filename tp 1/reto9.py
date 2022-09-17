# coding=utf-8

# RETO IX: Si ahora queremos hacer nuestro programa un poco más estricto, por cada vuelta deberíamos sumar el total de
#células que tenemos e imprimir ese número en el mensaje. Entonces, por ejemplo, como en la primer vuelta tenemos dos
#células, imprimimos como mensaje ‘¡Somos 2 clones!’ , pero en la segunda vuelta serán en total 4 células y el mensaje
#a imprimir debería ser ‘¡Somos 4 clones!’. ¿Podrías escribir esta modificación del programa?

def vuelta():
    n = 1
    for i in range(0,20):
        n = n*2
        print('¡Somos ' + str(n) +' clones nuevos!')

if __name__ == '__main__':
    vuelta()