# t3.py

class Producto:
  def __init__(self, no=None):
    self.no = no

Producto.categoria_general = "woeidndn"
Producto.impuesto_global = "iwuerbf"
glob = Producto("Glob")
glob.nombre = "glob"
glob.precio = 367248
glob.stock = False
glob.__dict__