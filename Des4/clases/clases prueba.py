class Atleta:
    nombre = ""
    def __init__(self, nombre:str):#custom function factory = constructor en java
                       #self = this
        self.nombre = nombre
    
    def display(self):
        print(f"{self.nombre}")
        
    def __str__(self):
        return f"Nombre del atleta: {self.nombre}"
    
    def __repr__(self):
        return f"Atleta({self.nombre})"
    

a = Atleta("Ana Guevara") # Atleta.__init(a, "Ana Guevara") # es lo mismo
a.display()
av = Atleta("Alejandra Valencia")
print(str(av))
print(repr(av), "\n")

class Figura:
    def __init__(self,lados):
        self.lados = lados
    def set_lado(self, lado):
        self.lado = lado
    def perimetro(self):
        if self.lado:
            return self.lado * self.lados
    def __str__(self):
        return f"El perimetro de figura con {self.lados} lados y una longitud de {self.lado} es igual a {self.perimetro()}"

c = Figura(4)
c.set_lado(6)
print(f"El perimetro de la figura es {c.perimetro()}")
print(str(c))





