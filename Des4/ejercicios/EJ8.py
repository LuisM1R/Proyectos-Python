#DEFINIR FUNCIONES

#sin definir tipo de dato
def producto(a,b):
  return a*b

#definiendo el tipo de dato
def suma(a:int, b:int) -> int:
  '''suma: recibe 2 enteros y regresa la suma de los 2'''
  return a+b

h=5; j=6
z= producto(h,j)

print(f"El producto de {h} y {j} es: {z}")
print(f"La Suma de {h} y {j} es:{suma(h,j)}")
print()


def coordenada_y(m:float, b:float, x:float)->float:
  '''coordenada y: Recibe pendiente e interseccion, el valor de x, y calcula posicion de y'''
  return m*x+b
  
print ("La coordenada en 'y' es", coordenada_y(2,1,0))
print()

pendiente = 2
intercepcion = 1

x = []
for n in range (0,10):
  x.append(n)
  
y =[]
for n in x:
  t = coordenada_y(pendiente, intercepcion, n)
  y.append(t)
  
print(x)
print(y)
print()

X = [n for n in range(0,10)]
cy = coordenada_y
Y = [cy(pendiente, intercepcion, n) for n in X]
coord = list(zip(X,Y))
print(coord)
print(X)
print(Y)
