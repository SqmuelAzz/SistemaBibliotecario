# controllers/loan_controller.py

from models.prestamo import Prestamo

class LoanController:
    def __init__(self):
        self.prestamos = []

    def registrar_prestamo(self, prestamo):
        if isinstance(prestamo, Prestamo):
            prestamo.registrar_prestamo()
            self.prestamos.append(prestamo)
            print(f"Préstamo {prestamo.id_prestamo} registrado.")

    def marcar_devolucion(self, prestamo):
        if isinstance(prestamo, Prestamo):
            prestamo.marcar_devolucion()
            print(f"Devolución del préstamo {prestamo.id_prestamo} registrada.")
