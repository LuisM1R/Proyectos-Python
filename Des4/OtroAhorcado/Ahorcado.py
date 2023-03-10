class Ahorcado:
    def __init__(self, palabra:str="ahorcado"):
        self.abc = [chr(x) for x in range(ord("A"),ord("Z")+1)]
        self.tablero = {}
        self.strikes = 0
        for i in range(0,7):
            self.leer_archivo_texto(f"ahorcado{i}.txt",i)
        self.lista_letras = [ [x,"-"] for x in palabra]

    def leer_archivo_texto(self, archivo:str,indice:int):
        ''' lee el archivo y regresa una lista de cadenas'''
        data = []
        try:
            with(open(archivo,'r',encoding="utf-8")) as a:
                data = a.readlines()
            data = [ linea.strip("\n") for linea in data ]
        except (FileNotFoundError, IOError):
            print(f"No existe el archivo '{archivo}'")   
        self.tablero[indice] = data

    def despliega(self):
        strikes = self.strikes
        tab = self.tablero[strikes]
        self.despliega_abc()
        self.despliega_lista_letras()
        for renglon in tab:
            print(renglon)

    def despliega_abc(self):
        cadena = "".join(self.abc)
        print(cadena)

    def despliega_lista_letras(self):
        cadena = "".join([x[1] for x in self.lista_letras] )
        print(cadena)

def main(archivo_fuente:str):
    fuente = FuentePalabras(archivo_fuente)

if __name__ == "__main__":
    A = Ahorcado()
    A.despliega()