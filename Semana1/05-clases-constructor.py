class Persona:
    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

miPersona = Persona("Mario", "02/09/1977")        

print(miPersona.nombre)

