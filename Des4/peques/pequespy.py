def main():
     #1. Generar un diccionario a partir de dos listas (hay un modo pitónico de hacerlo) e imprimirlo:
   
    print(primero())

    #2. Invierte una palabra sin utilizar el método reverse() e imprimirla

    print(segundo(input('Ingresa una palabra: \n')))

def primero() -> dict:
    ciudades = ["Hermosillo", "Ciudad Obregón", "Guaymas", "San Luis Río Colorado", "Navojoa"]   
    habitantes = [994000, 333000, 152000, 131000, 121000]
    diccionario = { ciudades[i]:habitantes[i] for i in range(len(ciudades)) }

    #diccionario = dict(zip(ciudades,habitantes))

    # for i in range(len(ciudades)):
    #     diccionario[ciudades[i]] = habitantes[i]
    return ''.join([f'{key} tiene {value} habitantes\n' for key,value in diccionario.items()])


def segundo(palabra:str):
    palabra_inv = palabra[::-1]
    return palabra_inv

if __name__ == "__main__":
    main()
