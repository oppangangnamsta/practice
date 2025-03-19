# tecnico.py
from empleado import Empleado

class Tecnico(Empleado):
    def __init__(self, nombre, identificacion, sueldo, horas_extra, tarifa_extra):
        super().__init__(nombre, identificacion, sueldo)
        self.horas_extra, self.tarifa_extra = horas_extra, tarifa_extra