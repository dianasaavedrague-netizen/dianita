#definicion de la clase estudiante
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Estudiante(nombre='{self.nombre}', edad={self.edad})"


# Crear 5 estudiantes
e1 = Estudiante("Carlos", 20)
e2 = Estudiante("Ana", 22)
e3 = Estudiante("Luis", 19)
e4 = Estudiante("Beatriz", 21)
e5 = Estudiante("Daniel", 23)

# Guardar en una lista
estudiantes = [e1, e2, e3, e4, e5]

# Ordenar la lista por nombre
estudiantes.sort(key=lambda estudiante: estudiante.nombre)

# Mostrar el resultado
for estudiante in estudiantes:
    print(estudiante)
