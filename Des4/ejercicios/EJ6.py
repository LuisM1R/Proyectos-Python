#Diccionarios

d = {}
dd = dict()

d['Alan'] = 'Star Wars'
d['Octavio'] = 'LaLaLand'
d['Adan'] = 'Atletico San Pancho'
d['Luis'] = 'Forrest Gump'

print(d)
print()
print('Pelicula favorita de Adan:', d['Adan'])
print()

lista = ['Alan', 'Adan', 'Mariana', 'Jesus', 'Octavio', 'Luis']

for persona in lista:
  if persona in d: #esta es la persona dic?
    print(f'La pelicula favorita de {persona} es {d[persona]}')
  else:
    print(f'{persona} no esta en el diccionario')
    
    #try except
print()
for persona in lista:
  try:
      print(f'La pelicula favorita de {persona}: {d[persona]}')
  except KeyError:
      print(f'{persona} no esta en le diccionario')

  