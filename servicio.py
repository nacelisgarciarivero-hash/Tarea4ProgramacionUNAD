from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError, ServicioNoDisponibleError
import logging

logging.basicConfig(filename="logs.txt", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

class Servicio ABC:
    
    def __init__ self, nombre, precio_base:
        self._nombre = None
        self._precio_base = None
        self.nombre = nombre
        self.precio_base = precio_base
    
    @property
    def nombre self:
        return self._nombre
    
    @nombre.setter
    def nombre self, valor:
        if not valor or len valor.strip == 0:
            error = DatoInvalidoError f"El nombre del servicio no puede estar vacío"
            logging.error str error
            raise error
        if len valor > 50:
            error = DatoInvalidoError f"El nombre del servicio excede 50 caracteres: valor"
            logging.error str error
            raise error
        self._nombre = valor.strip
    
    @property
    def precio_base self:
        return self._precio_base
    
    @precio_base.setter
    def precio_base self, valor:
        if not isinstance valor, int and not isinstance valor, float:
            error = DatoInvalidoError f"El precio base debe ser un número, se recibió type valor .__name__"
            logging.error str error
            raise error
        if valor <= 0:
            error = DatoInvalidoError f"El precio base debe ser mayor a cero, se recibió valor"
            logging.error str error
            raise error
        self._precio_base = valor
    
    @abstractmethod
    def calcular_costo self, impuesto=0.0, descuento=0.0, servicio_extra=None:
        pass
    
    @abstractmethod
    def describir self:
        pass
    
    def validar_disponibilidad self:
        try:
            disponible = self._verificar_disponibilidad
            if not disponible:
                raise ServicioNoDisponibleError f"El servicio self._nombre no está disponible en este momento"
            return True
        except ServicioNoDisponibleError as e:
            logging.error str e
            raise
        except Exception as e:
            logging.error f"Error inesperado al validar disponibilidad de self._nombre: str e"
            raise DatoInvalidoError f"No se pudo validar la disponibilidad del servicio" from e
    
    def _verificar_disponibilidad self:
        return True


class Sala Servicio:
    
    def __init__ self, nombre, precio_base, capacidad, tiene_proyector=False:
        super.__init__ nombre, precio_base
        self._capacidad = None
        self.tiene_proyector = tiene_proyector
        self.capacidad = capacidad
    
    @property
    def capacidad self:
        return self._capacidad
    
    @capacidad.setter
    def capacidad self, valor:
        if not isinstance valor, int:
            error = DatoInvalidoError f"La capacidad debe ser un número entero, se recibió type valor .__name__"
            logging.error str error
            raise error
        if valor < 1 or valor > 200:
            error = DatoInvalidoError f"La capacidad debe estar entre 1 y 200 personas, se recibió valor"
            logging.error str error
            raise error
        self._capacidad = valor
    
    def calcular_costo self, impuesto=0.0, descuento=0.0, servicio_extra=None:
        try:
            costo_base = self.precio_base
            if servicio_extra == "catering":
                costo_base += 150000
            elif servicio_extra == "audio":
                costo_base += 80000
            elif servicio_extra == "limpieza":
                costo_base += 50000
            costo_con_impuesto = costo_base * 1 + impuesto
            costo_final = costo_con_impuesto * 1 - descuento
            if costo_final <= 0:
                raise DatoInvalidoError "El costo final calculado es menor o igual a cero"
            return round costo_final, 2
        except DatoInvalidoError as e:
            logging.error str e
            raise
        except Exception as e:
            logging.error f"Error al calcular costo de sala self.nombre: str e"
            raise DatoInvalidoError f"No se pudo calcular el costo del servicio Sala" from e
    
    def describir self:
        proyector = "con proyector incluido" if self.tiene_proyector else "sin proyector"
        return f"Sala self.nombre con capacidad para self.capacidad personas proyector"


class Equipo Servicio:
    
    def __init__ self, nombre, precio_base, tipo_equipo, horas_estimadas=1:
        super.__init__ nombre, precio_base
        self._tipo_equipo = None
        self.horas_estimadas = horas_estimadas
        self.tipo_equipo = tipo_equipo
    
    @property
    def tipo_equipo self:
        return self._tipo_equipo
    
    @tipo_equipo.setter
    def tipo_equipo self, valor:
        tipos_validos = ["proyector", "computador", "tablet", "impresora", "sonido"]
        if valor.lower not in tipos_validos:
            error = DatoInvalidoError f"Tipo de equipo no válido. Tipos permitidos: tipos_validos"
            logging.error str error
            raise error
        self._tipo_equipo = valor.lower
    
    def calcular_costo self, impuesto=0.0, descuento=0.0, servicio_extra=None:
        try:
            costo_por_hora = self.precio_base
            costo_total = costo_por_hora * self.horas_estimadas
            if servicio_extra == "seguro":
                costo_total += costo_total * 0.10
            elif servicio_extra == "entrega_domicilio":
                costo_total += 30000
            costo_con_impuesto = costo_total * 1 + impuesto
            costo_final = costo_con_impuesto * 1 - descuento
            if costo_final <= 0:
                raise DatoInvalidoError "El costo final calculado es menor o igual a cero"
            return round costo_final, 2
        except DatoInvalidoError as e:
            logging.error str e
            raise
        except Exception as e:
            logging.error f"Error al calcular costo de equipo self.nombre: str e"
            raise DatoInvalidoError f"No se pudo calcular el costo del servicio Equipo" from e
    
    def describir self:
        return f"Equipo self.tipo_equipo llamado self.nombre por self.horas_estimadas horas estimadas"


class Asesoria Servicio:
    
    def __init__ self, nombre, precio_base, especialidad, duracion_horas=1:
        super.__init__ nombre, precio_base
        self._especialidad = None
        self.duracion_horas = duracion_horas
        self.especialidad = especialidad
    
    @property
    def especialidad self:
        return self._especialidad
    
    @especialidad.setter
    def especialidad self, valor:
        especialidades_validas = ["desarrollo", "redes", "seguridad", "datos", "nube"]
        if valor.lower not in especialidades_validas:
            error = DatoInvalidoError f"Especialidad no válida. Especialidades permitidas: especialidades_validas"
            logging.error str error
            raise error
        self._especialidad = valor.lower
    
    def calcular_costo self, impuesto=0.0, descuento=0.0, servicio_extra=None:
        try:
            costo_base = self.precio_base * self.duracion_horas
            if servicio_extra == "urgente":
                costo_base *= 1.5
            elif servicio_extra == "material_adicional":
                costo_base += 120000
            costo_con_impuesto = costo_base * 1 + impuesto
            costo_final = costo_con_impuesto * 1 - descuento
            if costo_final <= 0:
                raise DatoInvalidoError "El costo final calculado es menor o igual a cero"
            return round costo_final, 2
        except DatoInvalidoError as e:
            logging.error str e
            raise
        except Exception as e:
            logging.error f"Error al calcular costo de asesoria self.nombre: str e"
            raise DatoInvalidoError f"No se pudo calcular el costo del servicio Asesoria" from e
    
    def describir self:
        return f"Asesoría en especialidad self.especialidad llamada self.nombre por self.duracion_horas horas"
