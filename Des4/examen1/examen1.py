#EXAMEN1
#Luis Alberto Miranda Díaz 
#10am - 11am

#Escribir un programa en Python que lee un archivo de texto Heinlein_La_Luna.txt (anexo), 
#crea un diccionario de palabras de diferente tamaño e imprime el tamaño de la llave y el 
#número de palabras que tienen esa longitud. 

# Además, lee un archivo de texto llamado spanish_stopwords.txt (anexo) 
# y remueve cada ocurrencia de estas palabras en el texto anterior 
# e imprime el top ten de palabras que más aparecen en el texto.    

def leer_archivo(archivo:str)->str:
    with(open(archivo,"r",encoding ="utf-8")) as a:
            data = a.read() 
    return data

def limpia_texto(texto:str) -> str:
    conjunto = set(["\n",",",".",",",";",":","!","?","-","_","(",")", "¿", "¡", "»", "«", "♀", "'"])
    texto_limpio = "".join([x if x not in conjunto else " " for x in texto])
    return texto_limpio

def contar_palabras(texto:str)->dict:
    lista_palabras = texto.split(" ")
    d={} 
    for palabra in lista_palabras:
        if palabra in d:
            d[palabra] += 1
        else:
            d[palabra] = 1
    return d

def top10(texto:str, archivo) -> dict:
    
    numero = contar_palabras(texto)
    libro = leer_archivo(archivo)

    top = dict(zip(numero,libro))

    for palabra in top:
        if palabra in top:
            top[palabra] += 1
        else:
            top[palabra] = 1

    return top

def main(archivo, archivo2):
    archivo = "Heinlein_La_Luna.txt"
    archivo2 = "spanish_stopwords.txt"

    texto = leer_archivo("Heinlein_La_Luna.txt")
    texto_nuevo = limpia_texto(texto)
    newtext = texto_nuevo.lower()
    #print(newtext)

    listalibro = newtext.split()
    #print(listalibro)
    print()

    #for i 

    archivo2 = "spanish_stopwords.txt"
    texto2 =leer_archivo("spanish_stopwords.txt")

    listapalabras = texto2.split()
    #print(listapalabras)


    setlibro = set(listalibro)
    setpalabras = set(listapalabras)

    sinSpanish = setlibro.intersection(setpalabras)
    print(sinSpanish)

    print("Solo logré hacer una lista de en la que estan las palabras del libro sin las palabras del texto spanish")

    dp = contar_palabras(texto_nuevo)
    print(f"Total de palabras unicas:{len(dp)}")

    print()
    #print("EL top 10 de palabras que mas aparecen son: \n")
    #print(f'El numero {i} es {palabra}')





if __name__ == "__main__":
    archivo = "Heinlein_La_Luna.txt"
    archivo2 = "spanish_stopwords.txt"
    main(archivo, archivo2)