#!/bin/bash
function ayuda(){
	echo -e "EL juego de la vida consiste en un simulador del proceso de crear una proteína a partir de una cadena ADN."
	echo -e "Cada codón formado correctamente sumará puntos."
	echo -e "Una fase sera la de formar la cadena de ARNm y, en el nivel bonus, la cadena de Proteina."
	echo -e "Es necesario tener instalado Python para ejecutar el programa"
	echo -e "Escribe en la consola ./juegoDeLaVida.sh para poder jugar!"
	echo -e "diviertete!"
	}

if [ "$1" != "--help" ] && [ "$1" != "--h" ]
	then
		python3 juegoDeLaVida.py
	else
		ayuda
fi