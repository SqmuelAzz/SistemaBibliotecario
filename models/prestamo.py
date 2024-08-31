# models/prestamo.py

from datetime import datetime

class Prestamo:
    def __init__(self, id_prestamo, usuario, ejemplar, fecha_prestamo, fecha_devolucion, tipo_prestamo):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.ejemplar = ejemplar
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.tipo_prestamo = tipo_prestamo
        self.multa = None

    def registrar_prestamo(self):
        self.ejemplar.cambiar_estado("prestado")
        self.usuario.historial.append(f"Préstamo de ejemplar {self.ejemplar.id_ejemplar} realizado el {self.fecha_prestamo}")
        print(f"Préstamo {self.id_prestamo} registrado para el usuario {self.usuario.nombre_completo}")

    def marcar_devolucion(self):
        self.ejemplar.cambiar_estado("disponible")
        self.usuario.historial.append(f"Devolución de ejemplar {self.ejemplar.id_ejemplar} realizada el {datetime.now()}")
        print(f"Devolución del préstamo {self.id_prestamo} marcada.")

    def calcular_multa(self, dias_retraso):
        # Implementación básica para el cálculo de multas
        if dias_retraso > 0:
            monto_multa = dias_retraso * 5  # Ejemplo: 5 unidades por día de retraso
            self.multa = monto_multa
            print(f"Multa calculada: {monto_multa} unidades")
        else:
            self.multa = 0
            print("No hay multa.")
