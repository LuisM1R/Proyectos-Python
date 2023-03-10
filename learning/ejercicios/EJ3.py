lunas =['Luna', 'Deimos', 'Phobos', 'Ganimede']
print(lunas)

lunas.append('Io')#añade al final
print (lunas)

lunas.insert(2, 'Calixto')#añade en la posicion dicha
print(lunas)

lunas.remove('Calixto')#elimina al escrito
print(lunas)

lunas.append('Hoth')
print(lunas)

lunas.insert(3, 'Hoth')
print(lunas)

lunas.remove('Hoth')#Remove solo elimina a uno, de izquierda a derecha
print(lunas)

print(lunas.pop(1))#elimina el elemento especificado por el indice
print(lunas)

print(lunas.pop()) #sin especificar POP se elimina al ultimo elemento
print(lunas)

lunas.clear() #elimina todo
print(lunas)