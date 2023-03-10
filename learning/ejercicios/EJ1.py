#lista = []
#print(id(lista))
#print(dir(lista))

numeros = [3, 43, 5, 44, 356, 3246]
print(numeros)


numeros.append(3.14)
print(numeros)


numeros.append("pi")
print(numeros)


for n in numeros:
  print (n)


numeros.insert (0,10) 
#el 0 es la posicion, el 10 es el numero que insertamos
print (numeros)

numeros.insert(3,15)
print (numeros)

planetas = list()
planetas.append ("tierra")
planetas.append ("marte")
planetas.append ("jupiter")
planetas.append ("saturno")
planetas.append ("mercurio")
planetas.append ("venus")
print (planetas)
print (planetas[1])
print (planetas[0:4])

internos = planetas[0:3]
print (internos)