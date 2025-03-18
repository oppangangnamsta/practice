# gerente.py
from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, apellido, edad, departamento, bono):
        super().__init__(nombre, apellido, edad)
        self.departamento = departamento
        self.bono = bono