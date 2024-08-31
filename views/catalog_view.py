# views/catalog_view.py

from rich.console import Console
from rich.table import Table

class CatalogView:
    def mostrar_articulo(self, articulo):
        console = Console()
        table = Table(title=f"Artículo: {articulo.titulo}")

        table.add_column("Campo", justify="right", style="cyan", no_wrap=True)
        table.add_column("Valor", style="magenta")

        table.add_row("ID", str(articulo.id_articulo))
        table.add_row("Título", articulo.titulo)
        table.add_row("Autor", articulo.autor)
        table.add_row("Año de Publicación", str(articulo.ano_publicacion))
        table.add_row("Editorial", articulo.editorial)
        table.add_row("Categoría", articulo.categoria)
        table.add_row("Palabras Clave", ", ".join(articulo.palabras_clave))
        table.add_row("Cantidad", str(articulo.cantidad))

        console.print(table)
