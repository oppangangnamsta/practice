# t1.py

class PrismaRectangular():

  def __init__(self, altura, anchura, profundidad):
    self.altura = altura
    self.anchura = anchura
    self.profundidad = profundidad
  
  def calcula_volumen(self):
    return "volumen"
  
  def cambia_proporciones(self, escala):
    self.altura *= escala
    self.anchura *= escala
    self.profundidad *= escala