fila = ['Mariana', 'Daniel','Jorge', 'Carlos']
print (fila)
otraFila =['Pedro', 'Jesus', 'Jonathan', 'Ignacio', 'Alejandro']
print (otraFila)

print('Jorge' in fila)
print('Jorge' in otraFila)

print (fila.index('Jorge'))
#print(otraFila.index('Jorge'))

if 'Jorge' in otraFila:
  print(otraFila.index('Jorge'))
else:
  print('Jorge no se encuentra en la lista')

try:
  print(otraFila.index('Jorge'))
except ValueError:
  print('Jorge no se encuentra')

  
