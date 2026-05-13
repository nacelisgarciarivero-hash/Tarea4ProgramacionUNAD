# Clase Reserva
class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # Confirmar reserva
    def confirmar_reserva(self):

        self.estado = "Confirmada"

        return f"Reserva confirmada para {self.cliente}"

    # Cancelar reserva
    def cancelar_reserva(self):

        self.estado = "Cancelada"

        return f"Reserva cancelada para {self.cliente}"

    # Mostrar información
    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente}\n"
            f"Servicio: {self.servicio}\n"
            f"Duración: {self.duracion} horas\n"
            f"Estado: {self.estado}"
        )


# Ejemplo de uso

try:

    reserva1 = Reserva("Juan", "Spa", 2)

    print(reserva1.mostrar_reserva())

    print(reserva1.confirmar_reserva())

    print(reserva1.mostrar_reserva())

except ValueError as e:

    print("Error:", e)
