# models/reporte.py

class Reporte:
    def __init__(self, tipo_reporte, filtros):
        self.tipo_reporte = tipo_reporte
        self.filtros = filtros

    def generar_reporte(self):
        print(f"Generando reporte {self.tipo_reporte} con filtros {self.filtros}")


class ReporteBasico(Reporte):
    def exportar_reporte(self):
        print(f"Reporte básico exportado con filtros {self.filtros}")


class ReporteConExcel(Reporte):
    def exportar_reporte(self):
        print("Reporte exportado en formato Excel")


class ReporteConPDF(Reporte):
    def exportar_reporte(self):
        print("Reporte exportado en formato PDF")
