# controllers/catalog_controller.py

from models.articulo import Articulo

class CatalogController:
    def __init__(self):
        self.articulos = []

    def agregar_articulo(self, articulo):
        if isinstance(articulo, Articulo):
            self.articulos.append(articulo)
            print(f"Artículo {articulo.titulo} agregado al catálogo.")

    def buscar_articulo(self, titulo):
        resultado = [articulo for articulo in self.articulos if articulo.titulo == titulo]
        if resultado:
            print(f"Artículo '{titulo}' encontrado en el catálogo.")
        else:
            print(f"Artículo '{titulo}' no encontrado.")
