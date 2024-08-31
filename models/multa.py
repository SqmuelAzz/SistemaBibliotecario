# models/multa.py

class Multa:
    def __init__(self, id_multa, usuario, monto, dias_retraso):
        self.id_multa = id_multa
        self.usuario = usuario
        self.monto = monto
        self.dias_retraso = dias_retraso

    def calcular_multa(self):
        self.monto = self.dias_retraso * 5  # Ejemplo: 5 unidades por día de retraso
        print(f"Multa para {self.usuario.nombre_completo}: {self.monto} unidades.")

    def aplicar_multa(self):
        print(f"Multa aplicada a {self.usuario.nombre_completo}: {self.monto} unidades.")
