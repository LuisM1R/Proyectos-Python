diez = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cien =[]
for i in range(0, 100):
  cien.append(i)
  
print(diez)
print(cien)

cien_math = [x for x in range(0, 100)]
print(cien_math)

print(cien_math[0:50])#imprime los numeros de ese indice

print(cien_math[0:50:2])#imprime los numeros de ese indice con intervalos de 2

print(cien_math[:50:2])#no es necesario especificar el 0

print(cien_math[::10])#saltos de intervalos de la lista

print(cien_math[::-1])#lista al reves

print(cien_math[::-2])# lista al reves con intervalos

print(cien_math)
diez.extend(cien)#concatenar los elementos de cien a la lista de cien
print(diez)

print(diez[-1])#muestra el ultimo elemento
print(diez[-5])#muestra el elemento dicho al reves
print(diez[5])#muestra el elemento del indice dicho




