def leer_archivo(archivo:str)->str:
    with(open(archivo,"r",encoding ="utf-8")) as a:
            data = a.read() #un solo texto(str)
    return data

def contar_palabras(texto:str)->dict:
    lista_palabras = texto.split(" ")
    d={} # diccionario
    for palabra in lista_palabras:
        if palabra in d:
            d[palabra] += 1
        else:
            d[palabra] = 1
    return d

def limpia_texto(texto:str) -> str:
    conjunto = set(["\n",",",".",",",";",":","!","?"])
    texto_limpio = "".join([x if x not in conjunto else " " for x in texto])
    return texto_limpio

def escribe_csv(lista:list, archivo:str) -> None:
    with(open(archivo, "w")) as a:
        for palabra in lista:
            if len(palabra[0]) > 4:
                a.write(palabra[0])
                a.write("\n")
    
def main(archivo):
    archivo = "las_mil_y_una_noches.txt"
    texto = leer_archivo(archivo)
    texto_nuevo = limpia_texto(texto)
    dp = contar_palabras(texto_nuevo)
    print(f"Archivo: {archivo}")
    print(f"Total de palabras unicas:{len(dp)}")
    lista = [(key,valve) for key, valve in dp.items()]
    archivo_salida = "lista_palabras.txt"
    escribe_csv(lista,archivo_salida)

if __name__ == "__main__":
    archivo = "las_mil_y_una_noches.txt"
    main(archivo)