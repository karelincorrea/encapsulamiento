class Persona:

    def __init__(self, nombre:str, apellido:str, cedula:str, correo:str, edad:int = None, vip:bool = False, fecha_nacimiento=None ):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._cedula = cedula
        self._correo = correo
        self._vip = vip
        self._fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f'Persona {self.__dict__.__str__()}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def cedula(self):
        return self.cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def correo(self):
        return self.correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def vip(self):
        return self.vip

    @vip.setter
    def vip(self, vip):
        self._vip = vip

    @property
    def fecha_nacimiento(self):
        return self.fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self,fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento



p1 = Persona(cedula='0963476854', nombre='Karelin ', apellido='Correa', correo='karelin23@gmail.com', edad=26)
print(p1)