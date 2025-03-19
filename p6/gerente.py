# gerente.py
from empleado import Empleado

class Gerente(Empleado):
    """
    A class used to represent an empleado

    Attributes
    ----------
    nombre : str
        nombre del empleado
    identificacion : int
        identificacion del empleado
    sueldo : int
        sueldo del empleado
    departamento : str
        departamento del empleado
    """
    def __init__(self, nombre, identificacion, sueldo, departamento, bono):
        super().__init__(nombre, identificacion, sueldo)
        self.departamento = departamento
        self.bono = bono

    def calcular_sueldo_final(self):
        return self.sueldo * self.bono