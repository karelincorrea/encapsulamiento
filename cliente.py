class Cliente:
    contador_cliente = 0

    def __init__(self, nombre, apellido, fecha_registro, vip):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_registro = fecha_registro
        self._vip = vip
        Cliente.contador_cliente += 1
        self._id_cliente = Cliente.contador_cliente

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    def _str_(self):
        return f'Cliente: {self.__dict.str__()}'

if __name__ == '__main__':
    cli1 = Cliente(nombre='Gianna', apellido='Santamaria', fecha_registro='13-10-2020', vip= True)
    print(cli1)
    cli2 = Cliente(nombre='Lady', apellido='Rezabala', fecha_registro='14-01-2023', vip= False)
    print(cli2)