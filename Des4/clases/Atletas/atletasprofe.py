from Atleta import Atleta
from csv import reader
from numpy import arange
from random import choice

def cargar_atletas(archivo):
    atletas = {}
    with open(archivo, "r", encoding="utf-8") as a:
        csv_reader = reader(a)
        for linea in csv_reader:
            nombre = linea[0]
            edad = int(linea[1])
            atleta = Atleta(nombre, edad)
            atletas[nombre] = atleta
    return atletas

def carrera(atletas:dict, valores:list):
    for nombre, atleta in atletas.items():
        t = round(choice(valores),1)
        atleta.agregar_tiempo(t)

def ganador(atletas:dict):
    top = 19.2
    key = ""
    for nombre, atleta in atletas.items():
        t = atleta.ultimo()
        if atleta.ultimo() < top:
            top = atleta.ultimo()
            key = nombre
        print(f"{nombre} - Tiempo:{atleta.ultimo()}")
    print(f"\n-----------Gana: {key} con {top} segundos-------------\n")
    return key

def main(juegos = 10):
    atletas = cargar_atletas("atletas.csv")
    valores = [x for x in arange(9.6, 19.2, 0.1)]   
    contador = 0
    lista = []
    while contador < juegos:
        carrera(atletas, valores)
        gana =ganador(atletas)
        print(atletas[gana])
        lista.append(gana)
        contador +=1
    print(str(lista) +"\n")

if __name__ == "__main__":
    main()