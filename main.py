from cliente import Cliente
from servicio import Sala, Equipo, Asesoria
from reserva import Reserva

def guardar_log(error):
   with open("logs.txt", "a") as f:
       f.write(error + "\n")

print("INICIO DEL SISTEMA")

# Caso correcto
try:
   cliente1 = Cliente("Juan", "juan@test.com", "123456")
   servicio1 = Sala("Sala VIP", 100)

   reserva1 = Reserva(cliente1, servicio1)
   reserva1.confirmar()

   print(reserva1.mostrar())

except Exception as e:
   print("Error:", e)
   guardar_log(str(e))


# Caso incorrecto
try:
   cliente2 = Cliente("", "correo_malo", "abc")
except Exception as e:
   print("Error:", e)
   guardar_log(str(e))
