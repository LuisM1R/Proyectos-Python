import os
import string

def main():
    print("1. Generar un diccionario a partir de dos listas (hay un modo pitónico de hacerlo) e imprimirlo: \n")
    ciudades = ["Hermosillo", "Ciudad Obregón", "Guaymas", "San Luis Río Colorado", "Navojoa"]   
    habitantes = [994000, 333000, 152000, 131000, 121000]
    diccionario = { ciudades[i]:habitantes[i] for i in range(len(ciudades)) }
    print(''.join([f'{key} tiene {value} habitantes\n' for key,value in diccionario.items()]))

    print("2. Invierte una palabra sin utilizar el método reverse() e imprimirla \n")
    print('Ingresa una palabra:')
    palabra = input() 
    palabra_inv = palabra[::-1]
    print(palabra_inv)
    print()

    print("3. Imprime 3 emojis \n")
    print("🤣")
    print("🥰")
    print("🤔\n")

    print("4. Utiliza el módulo string para remover de una forma fácil y sencilla signos de puntuación e imprimirla.")
    texto = 'He hecho cosas que ustedes las personas no podrían ni imaginar. sAtaqué naves con fuego en las colonias interplanetarias. He visto estrellas brillar en la noche con mil colores. Todos esos momentos se perderán en el tiempo, como lágrimas bajo la lluvia.'
    texto_limpio = ''.join([x if x not in string.punctuation else '' for x in texto])
    print(texto_limpio)
    print()

    print("5. Utiliza la instrucción set() para encontrar la intersección entre listas:")
    
    CienciaFiccion = ["Star Wars", "Alien", "The Black Hole", "Star Trek 3", "Gravity", "Inception", "Dune", "Blade Runner", "Ready Player One"]
    PremiadasOscar = ["Casablanca", "The Hurt Locker", "Star Wars", "Alien", "Argo", "Unforgiven", "Gravity", "The silence of the lambs", "Dune", "Coda", "No country for old men", "Shakespeare in love", "Slumdog Millionare", "The Departed", "Million Dollar Baby", "Rain Man", "Inception"]

    CienciaFiccionSet = set(CienciaFiccion)
    PremiadasOscarSet = set(PremiadasOscar)
    interseccion =  CienciaFiccionSet.intersection(PremiadasOscarSet)
    print(interseccion)
    print()

    print("6. Utiliza el módulo os, para imprimir:")
    print("-------el directorio de trabajo actual (current working directory)")
    print(os.getcwd())
    print()

    print("-------la ruta o sendero para encontrar un archivo")
    archivo = 'photo1.jpg'
    for dirpath,dirname,filenames in os.walk('C:/Users/luism/Downloads/'):
        if archivo in filenames:
            path = dirpath
    
    print(f'La ruta para {archivo} es {path}')
    print()

    print("-------checar si un archivo en el directorio actual es archivo o folder")
    if os.path.isfile('ProgramaspyMDLA.py') == True:
        print(f'El elemento en {path} es un archivo')
    else:
        print(f'El archivo en {path} es un folder')


if __name__ == "__main__":
    main()
