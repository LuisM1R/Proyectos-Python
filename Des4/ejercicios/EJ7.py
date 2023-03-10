planetas = { 'Mercurio': 0,
          'Venus': 0,
          'Tierra': 1,
          'Marte': 2,
         'Jupiter': 79,
         'Saturno': 82,
          'Urano': 27,
         'Neptuno': 14}

for llave, valor in planetas.items():
  print(f'{llave} tiene {valor} satelites')

Mercurio = []
Venus =[]
Tierra = ['Luna']
Marte = ['Deimos', 'Phobos']
Jupiter = ['Io', 'Europa', 'Ganymede', 'Calisto']
Saturno = ['Titan', 'Thetis', 'Mimas', 'Enceladus', 'Dione']
Urano =['Miranda', 'Ariel', 'Titania', 'Puck']
Neptuno = ['Triton', 'Nereida']
Satelites = {'Mercurio': Mercurio, 
            'Tierra': Tierra,
            'Marte':Marte,
             'Jupiter': Jupiter,
             'Saturno': Saturno,
             'Urano': Urano,
             'Neptuno': Neptuno,
            }
print()
print('Satelites de Jupiter:', Satelites['Jupiter'])
print(f"Numero de satelites de Jupiter: {planetas['Jupiter']}")

Hermosillo = {
  'poblacion':812000,
  'superficie':168.2,
  'elevacion':400,
}
Obregon = {
  'poblacion':433050,
  'superficie': 12206,
  'elevacion': 400,
}
Guaymas = {
  'poblacion': 156863,
  'superficie':12206,
  'elevacion':10
}
Nogales = {
  'poblacion':26137,
  'superficie':16074,
  'elevacion':1200
}
Ciudades = {
  'Hermosillo': Hermosillo,
  'Obregon': Obregon,
  'Guaymas': Guaymas,
  'Nogales': Nogales
}
print()
print()

for pob, valor in Ciudades.items():
  print(f"La poblacion de {pob} personas es {Ciudades[pob]['poblacion']} y   su superficie es de :  {Ciudades[pob]['superficie']} km2 ")

print()
lista = [Hermosillo, Guaymas, Obregon, Nogales]
print(lista)

print()
print('dame el numero a')
a =input()
print('dame el numero b')
b = input()
def multiplica(a,b):
  return eval(a+'*'+b)

print(multiplica(a,b))



