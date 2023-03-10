from Ahorcado import Ahorcado
from FuentePalabras import FuentePalabras
import optparse


def main(archivo_fuente:str):
    fuente = FuentePalabras(archivo_fuente)
    en_juego=True
    juegos = { "Ganados":0,"Perdidos":0 }
    while en_juego:
        print(f"Ganados:{juegos['Ganados']} Perdidos:{juegos['Perdidos']}")
        palabra  = fuente.obtener_palabra()
        ahorcado = Ahorcado(palabra)
        ganado   = ahorcado.jugar()
        if ganado == True:
            juegos["Ganados"] += 1
        else:
            juegos["Perdidos"] += 1
        continuar = input("¿Desea seguir jugando? (S/N):")
        continuar = continuar.upper()
        if continuar == "S":
            en_juego = True
        else:
            en_juego = False
    print(f"Ganados:{juegos['Ganados']} Perdidos:{juegos['Perdidos']}")
    print("¡Gracias por jugar!")




if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option('-f','--fuente',dest='fuente',help='archivo de texto como fuente de palabras',
                      default='Heinlein_La_Luna.txt')
    (options,args) = parser.parse_args()

    main(options.fuente)