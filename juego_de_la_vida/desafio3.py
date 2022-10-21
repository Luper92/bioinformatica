import re
import sys

def getDatos(ruta_archivo):
    archivo = open(ruta_archivo, "r")
    datos = archivo.read()
    ##print(datos)
    datos = datos.split(":")
    archivo.close()

    ##new_args = arg
    ##print(new_args)
    return datos

##result = { i for i in d if i.startswith("TATAA")}
##print(result)

def filter(chain):
    print("cadena ingresada: ")
    print(chain)
    find = False
    newchain = ""
    for i in chain:
        result = re.search('TATAA(.*)TATAA', i)
        if result != None:
            find = True
            ##newchain.append(result.group(1))
            newchain = result.group(1)

    if(find):
        print("cadena de caja TATA: ")
        print(newchain)
    else:
        print("No hay caja TATA")





d = getDatos("info.txt")
filter(d)