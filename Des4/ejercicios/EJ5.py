lunas = ['Luna', 'Deimos', 'Phobos', 'Io', 'Europa']
planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Neptuno', 'Urano']

sistema_solar = [lunas, planetas]
print(sistema_solar) #se pueden crear listas de listas
print()

print(planetas)
print()

print(type(lunas), type(planetas), type(sistema_solar)) #nos dice que tipo de objeto es
print()

#objetos = lunas # el '=' crea una referencia a otro objeto
#objetos.extend(planetas)
#print(objetos)
#print(lunas) # se imprime lo mismo que en objetos, porq son los mismo
#print(id(lunas), id(objetos))#misma referencia

print()
celestiales = lunas.copy() #copiamos todo lo de lunas a celestiales sin afectar a lunas
celestiales.extend(planetas)
print(celestiales)
print(lunas)






