# Clase Servicio
from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass


class Sala(Servicio):
    def calcular_costo(self):
        return self.precio * 1.1


class Equipo(Servicio):
    def calcular_costo(self):
        return self.precio * 1.2


class Asesoria(Servicio):
    def calcular_costo(self):
        return self.precio * 1.3
