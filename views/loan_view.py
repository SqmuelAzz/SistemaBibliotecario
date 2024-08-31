# views/loan_view.py

from rich.console import Console
from rich.table import Table

class LoanView:
    def mostrar_prestamo(self, prestamo):
        console = Console()
        table = Table(title=f"Préstamo: {prestamo.id_prestamo}")

        table.add_column("Campo", justify="right", style="cyan", no_wrap=True)
        table.add_column("Valor", style="magenta")

        table.add_row("ID Préstamo", str(prestamo.id_prestamo))
        table.add_row("Usuario", prestamo.usuario.nombre_completo)
        table.add_row("Ejemplar", str(prestamo.ejemplar.id_ejemplar))
        table.add_row("Fecha de Préstamo", str(prestamo.fecha_prestamo))
        table.add_row("Fecha de Devolución", str(prestamo.fecha_devolucion))
        table.add_row("Tipo de Préstamo", prestamo.tipo_prestamo)
        if prestamo.multa:
            table.add_row("Multa", str(prestamo.multa))

        console.print(table)
