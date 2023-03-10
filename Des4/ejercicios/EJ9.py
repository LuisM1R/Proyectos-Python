def lee_archivo(archivo:str) -> list:
    with(open(archivo,"r")) as a:
          data = a.readlines()
    return data

don = "don_quijote.txt"
donquijote = lee_archivo(don)

print(type(donquijote))
print(len(donquijote))
print()
cadena = donquijote[1000]
print(donquijote[1000])
print()
lista = cadena.split(" ")
print(lista)
print()
cadena = cadena.strip("\n")
lista = cadena.split(" ")
print(lista)

def leer_archivo(archivo:str) -> str:
    with(open(archivo,"r")) as a:
      data = a.read()
    return data

donquijote = leer_archivo(don)
print()
print(len(donquijote))
print()
print(donquijote[0:1200])
print()

print(type(donquijote))
print()

donquijote = donquijote.strip('\n')
print(donquijote[1000:1200])


