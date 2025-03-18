# empleado.py

class Empleado:
    """
    A class used to represent an employee

    Attributes
    ----------
    nombre : str
        nombre del empleado
    identificacion : int
        identificacion del empleado
    sueldo : int
        sueldo del empleado

    Methods
    -------
    mostrar_informacion()
        muestra la informacion del empleado
    calcular_sueldo_final()
        calcula el sueldo final ( no )
    """

    def __init__(self, nombre, identificacion, sueldo):
        """
        Parameters
        ----------
        nombre : str
            nombre del empleado
        identificacion : str
            identificación del empleado
        sueldo : str
            sueldo del empleado
        """

        self.nombre, self.identificacion, self.sueldo = nombre, identificacion, sueldo

    def mostrar_informacion(self):
        print(f'''
        Nombre: {self.nombre}
        Identificacion: {self.identificacion}
        Sueldo: {self.sueldo}''')

    def calcular_sueldo_final(self):
        return self.sueldo