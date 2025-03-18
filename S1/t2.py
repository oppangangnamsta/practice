# t2.py

class Estudiante():

  escuela = "Harvard"
  def __init__(self, nombre, edad, curso):
    self.nombre = nombre
    self.edad = edad
    self.curso = curso
  
  def __str__(self):
    return f"me gusta el pollo -{self.nombre}"