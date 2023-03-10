import optparse

def lee_archivo_texto(nombre_archivo:str) -> str:
    '''Recibe un nombre de archivo e intenta leerlo, regresando el texto'''
    data =""
    with open(nombre_archivo,'r',encoding = "utf-8") as fh:
        data = fh.read()
    return data

def main(archivo:str, caracteres:int) -> None:
    '''recibimos un archivo y lo leemos'''
    texto = lee_archivo_texto(archivo)
    print(texto[0:200])

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-a","--archivo", type="str", help = "Archivo de texto leer")
    parser.add_option("-c", "--caracteres", dest="caracteres", type = "int", default = 0, 
                      help = "Numero de caracteres a mostrar, 0 = todo el texto")
    (opciones,args) = parser.parse_args()
    if opciones.archivo != None:
        if opciones.caracteres == 0:
            caracteres = -1
        else:
            caracteres = opciones.caracteres
        main(opciones.archivo, caracteres)
    else:
        parser.print_usage()
        #print(parser.usage())
