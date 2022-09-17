# coding=utf-8


# RETO VIII: Si nos ponemos un poco más estrictos, y siguiendo con el tema de los clones
# de bacterias, el programa que creamos antes tiene algunas fallas ‘numéricas’: en cada vuelta
# de división celular binaria se generarán dos clones,no uno.
# ¿Podrías escribir un programa que imprima ‘¡Somos 2 clones nuevos!’ en cada una de 20 vueltas? ¡Compartinos
# tu código en nuestro grupo de Facebook ‘Talleres de programación Orientada a la Biologia - SBG_UNQ’!

def vuelta():
    for i in range(0,20):
        print('¡Somos 2 clones nuevos!')

if __name__ == '__main__':
    vuelta()