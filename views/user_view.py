# views/user_view.py

from rich.console import Console
from rich.table import Table

class UserView:
    def mostrar_usuario(self, usuario):
        console = Console()
        table = Table(title="Información del Usuario")

        table.add_column("Campo", justify="right", style="cyan", no_wrap=True)
        table.add_column("Valor", style="magenta")

        table.add_row("Identificación", str(usuario.identificacion))
        table.add_row("Nombre", usuario.nombre_completo)
        table.add_row("Dirección", usuario.direccion)
        table.add_row("Celular", usuario.celular)
        table.add_row("Correo", usuario.correo)
        table.add_row("Fecha de Nacimiento", str(usuario.fecha_nacimiento))
        table.add_row("Ocupación", usuario.ocupacion)
        table.add_row("Centro de Estudio", usuario.centro_estudio)

        console.print(table)

    def mostrar_historial(self, usuario):
        console = Console()
        console.print(f"Historial de {usuario.nombre_completo}:")
        for entry in usuario.historial:
            console.print(entry)
