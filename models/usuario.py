# models/usuario.py

from datetime import datetime

class Usuario:
    def __init__(self, identificacion, nombre_completo, direccion, celular, correo, fecha_nacimiento, ocupacion, centro_estudio):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.celular = celular
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.ocupacion = ocupacion
        self.centro_estudio = centro_estudio
        self.estado = 'activo'
        self.historial = []

    def registrar(self):
        # Registrar un nuevo usuario
        print(f"Registrando usuario {self.nombre_completo}")

    def validar_datos(self):
        # Validar datos del usuario
        if '@' not in self.correo:
            raise ValueError("Correo electrónico no válido")
        if len(self.celular) < 10:
            raise ValueError("Número de celular no válido")
        print("Datos validados correctamente")

    def consultar_historial(self):
        # Consultar el historial de préstamos
        for entry in self.historial:
            print(entry)

    def pagar_multa(self, monto):
        # Pagar multa
        print(f"{self.nombre_completo} ha pagado una multa de {monto} unidades.")
