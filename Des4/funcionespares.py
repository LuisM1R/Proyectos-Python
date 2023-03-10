#     from random import choice

# def main():
#     mazo = crear_mazo()   
#     print()

#     jugador = sorted(obten_mano(mazo))
#     print("EL MAZO DEL JUGADOR:")
#     print(jugador, '\n')

#     compu = sorted(obten_mano(mazo))
#     print("EL MAZO DE LA COMPU:")
#     print(compu, '\n')

#     dvalores = {'2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14,'?':0}

#     # conteo = crea_conteo(compu)
#     # asigna_joker(conteo)

#     ganador(jugador, compu)
    

#     #for carta in mazo:
#     #    print(''.join(carta))


# def ganador(jugador:list, compu:list):
#     j = contar_puntos(jugador)
#     c = contar_puntos(compu)
#     print("RESULTADO:")
#     if j > c:
#         print("Ganó jugador")
#     else:
#         if j < c:
#             print("Ganó computadora")
#         else:
#             print("Empate")

# def crear_mazo() -> list:

#     numeros = [f"{x}" for x in range(2,11)]
#     letras = ["J", "Q", "K", "A"]
#     simbolos = ["❤", "◆", "☘", "♠"]
#     numeros.extend(letras)
#     mazo = []

#     for s in simbolos:
#         for n in numeros:
#             mazo.append([n,s])
#     jokers = ["?", "?"]
#     mazo.extend(jokers)   
#     return mazo

# def contar_puntos(jugador:list) -> int:
#     diccionario = {}
#     for carta in jugador:
#         if carta[0] in diccionario:
#             diccionario[carta[0]] += 1
#         else:
#             diccionario[carta[0]] = 1
    
#     puntos = 0
#     for k, v in diccionario.items():
#         if v == 2:
#             if k in ['J','Q','K']:
#                 puntos += 11
#             if k == 'A':
#                 puntos += 12
#             else:
#                 puntos += int(k)

#         if v == 3:
#             if k in ['J', 'Q', 'K']:
#                 puntos += 110
#             if k == 'A':
#                 puntos += 120
#             else:
#                 puntos += (int(k)*10)
#     return puntos

# def obten_carta(mazo:list): 
#     carta = choice(mazo)
#     mazo.remove(carta)
#     return carta

# def obten_mano(mazo:list) -> list:
#     mano = []
#     for i in range(0,5):
#         carta = obten_carta(mazo)
#         mano.append(carta)
#     return mano

# def asigna_joker(dconteo:dict, dvalores:dict):
#     if '?' in dconteo:
#         conteo_max = max(dconteo)
#         if conteo_max == 1:
#             llave = ""
#             maximo = 0
#             for k,v in dconteo.items():
#                 valor = dvalores[k]
#                 if valor > maximo:
#                     maximo = valor
#                     llave = k
#             dconteo[llave] += 1
#             del(dconteo['?'])

# def crea_conteo(mano:list) -> dict:
#     d = {}
#     for carta in mano:
#         if carta[0] in d:
#             d[carta[0]] += 1
#         else:
#             d[carta[0]] = 1
#     return d


# #if __name__ == "__main__":
# main() 