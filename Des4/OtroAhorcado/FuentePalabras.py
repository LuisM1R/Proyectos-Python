from Ahorcado import Ahorcado
#import unicode
import string

class FuentePalabras:
    '''Clase que lee un cuerpo de texto, lo separa en palabras
       y regresa una palabra al azar'''
    def __init__(self, archivo:str):
        '''iniciar clase'''
        self.nombre = archivo
        self.leer_archivo_texto(archivo)


    def leer_archivo_texto(self, archivo:str):
        '''lee archivo y regresa cadena de caracteres'''
        data = ""
        try:  
            with(open(archivo,"r",encoding ="utf-8")) as a:
                data = a.read() 
        except(FileNotFoundError, IOError):
             print("Archivo no encontrado {archivo}")
        self.texto = data

    def desplegar_nombre(self):
        print(self.nombre)
    
    def desplegar_texto(self):
         print(self.texto[0:200])
           
    def limpiar_texto(self):
        '''modifica cadena de texto, convierte a mayúsculas y remueve caracteres'''
        #mayusculas
        self.texto = self.texto.upper()
        #remover puntuacion
        self.texto = self.texto.translate(str.maketrans('', '',string.punctuation))
        lista_caracteres = ["<<", ">>", "¿", "?", "¡", "!" ]
        #remover caracteres
        for caracter in lista_caracteres:
            self.texto = self.texto.replace(caracter, '')
        #quitar acentos
        self.texto = unicode.unicode(self.texto)
        return self.texto

    def crear_diccionario(self):
           '''crea un diccionario de palabras desde una cadena'''
        #self.texto.split()
    
    def obtener_palabra(self):
           '''elige una palabra al azar del diccionario'''
        #random.choice


if __name__ == "__main__":
    archivo_fuente  = FuentePalabras("Heinlein_La_Luna.txt")
    archivo_fuente.desplegar_nombre()
    archivo_fuente.desplegar_texto()

    #palabra = fuente.obtener_palabra()