class Cliente:
    def __init__(self, nombre, correo, telefono):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        if not telefono.isdigit():
            raise ValueError("Teléfono inválido")

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def mostrar(self):
        return f"Cliente: {self.__nombre}, Correo: {self.__correo}, Tel: {self.__telefono}"
