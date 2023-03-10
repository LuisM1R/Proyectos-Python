#MIRANDA DIAZ LUIS ALBERTO 
#Programa Ahorcado con juego recurrente

import random
import os

def leer_archivo(archivo:str)->str:
    data = []
    with(open(archivo,"r",encoding ="utf-8")) as a:
            data = a.readlines() #un solo texto(str)
            data = [cadena.strip("\n")
                for cadena in data]
    return data

def main(archivo):
    lista_palabras = leer_archivo(archivo)
    #print(palabra)
    tableros = leer_tablero(6)
    respuesta = "si"
    score = {"Ganados": 0, "Perdidos": 0}
    while respuesta == "si":
        adivina(lista_palabras,tableros,score)
        respuesta = input("¿Quieres volver a jugar? si/no ")
        if respuesta != "si":
            print("Fin del juego")
            break


def leer_tablero(n:int) -> dict:
    d = {}
    for i in range (0, n+1):
        d[i] = leer_archivo(f"ahorcado-{i}.txt")
    return d

def despliega_tablero(tablero:list) -> None:
    for renglon in tablero:
        print(renglon)

def adivina(lista_palabras:list, tableros:dict, score:dict)->None:
    palabra = random.choice(lista_palabras)
    palabra = palabra.upper()
    #print(palabra)
    lista_letras = [[x,"_"] for x in palabra]
    abecedario = {chr(x):chr(x) for x in range (ord('A'), ord('Z')+1)}
    strikes = 0
    en_juego = True
    
    while en_juego == True:
            despliega_palabra(lista_letras)
            despliega_abc(abecedario)
            despliega_tablero(tableros[strikes])
            completa = True
            for lista in lista_letras:
                if lista[1] == "_":
                    completa = False
                    break
            if completa:
                en_juego = False
                print(f"La palabra era: {palabra}")
                print("Eres Ganador! :D")
                score['Ganados']+=1
                break
            else:
                if strikes == 6:
                    en_juego = False
                    print(f"La palabra era: {palabra}")
                    print("Eres Perdedor :C")
                    score['Perdidos']+=1
                    break
            letra = input("Adivina una letra: ")
            letra = letra.upper()
            if len(letra) != 1:
                continue
            else:
                intento = False
                for lista in lista_letras:
                    if letra == lista[0]:
                        lista[1] = letra
                        intento = True
                if intento == False:
                    strikes += 1
                if letra in abecedario:
                    abecedario[letra] = "*"
    os.system('cls')
    print(score)
                    
def despliega_palabra(lista_letras:list):
    lista = [x[1] for x in lista_letras]
    palabra = " ".join(lista)
    print(palabra)

def despliega_abc(diccionario:dict) -> None:
    abc = [value    for key, value in diccionario.items()]
    abc = "".join(abc)
    print(abc)

if __name__ == "__main__":
    archivo = "palabras.txt"
    main(archivo)
