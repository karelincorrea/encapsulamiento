from persona import Persona

class Empleado(Persona):

    def __init__(self, id_empleado, sueldo, nombre, apellido, cedula):
        self._id_empleado = id_empleado
        self._sueldo = sueldo
        self._nombre = nombre
        self._apellido = apellido
        self.cedula = cedula


    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, id):
        self._id_empleado = id

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo = sueldo


    def __str__(self):
        return f'Empleado {self.__dict__.__str__()}'

if __name__ == '__main__':
    e1 = Empleado(nombre='Leo', apellido='Roldan', sueldo='1500', cedula='0954869447', id_empleado=1)
    print(e1)