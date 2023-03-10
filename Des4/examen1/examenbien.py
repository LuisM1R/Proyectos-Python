import string
def main():
    archivo = "Heinlein_La_Luna.txt"
    texto = leer_texto(archivo)
    texto_limpio = limpia_texto(texto)
    dict_conteo =contar_palabras(texto_limpio)

    print(f"Longitud palabra    Cantidad")
    for key, value in sorted(dict_conteo.items()):
        print(f" {key:2}          {value:7}")
    
    #segunda parte
    archivo_palabras = "spanish_stopwords.txt"
    palabras = leer_texto(archivo_palabras)
    top10 = crea_top10(texto_limpio,palabras)
    for key, value in sorted(top10.items(), reverse = True)[0:10]:
        print(f" {key}    {value}")


def leer_texto(archivo:str) -> str:
    """Recibe un nombre de archivo y regresa su contenido"""
    data = ""
    with open(archivo,"r",encoding = "utf-8") as a:
        data = a.read()
    return data

def limpia_texto(texto:str) -> str:
    """Recibe una cadena de texto y la limpia"""
    lista_limpia = []
    for c in string.punctuation:
        texto = texto.replace(c,"")
    return texto

def contar_palabras(texto:str) -> dict:
    lista_palabras = texto.split(" ")
    diccionario = {}
    for palabra in lista_palabras:
        longitud = len(palabra)
        if longitud in diccionario:
            diccionario[longitud] += 1 #actualizamos
        else:
            diccionario[longitud] = 1 #creamos
    return diccionario

def crea_top10(texto:str, palabras:str) -> dict:
    lista_palabras_texto = texto.split(" ")
    lista_stopwords = palabras.split("\n")
    stopwords = set(lista_stopwords)
    nueva_lista = []
    for palabra in lista_palabras_texto:
        if palabra not in stopwords:
            nueva_lista.append(palabra)
    diccionario = {}
    for palabra in nueva_lista:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario


if __name__ == "__main__":
    main()
