from datetime import datetime

class RegistroTXT:

    def __init__(self, archivo="logs.txt"):
        self.archivo = archivo

    def registrar_evento(self, mensaje):

        with open(self.archivo, "a", encoding="utf-8") as file:

            fecha = datetime.now()

            file.write(f"[EVENTO] {fecha} - {mensaje}\n")

    def registrar_error(self, error):

        with open(self.archivo, "a", encoding="utf-8") as file:

            fecha = datetime.now()

            file.write(f"[ERROR] {fecha} - {error}\n")


log = RegistroTXT()

log.registrar_evento("Cliente registrado correctamente")

log.registrar_error("Correo inválido")

print("Datos guardados en logs.txt")
