# models/articulo.py

class Ejemplar:
    def __init__(self, id_ejemplar, estado="disponible"):
        self.id_ejemplar = id_ejemplar
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado


class Articulo:
    def __init__(self, id_articulo, titulo, autor, isbn, editorial):
        self.id_articulo = id_articulo
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.editorial = editorial
        self.ejemplares = []  # Inicializa como lista vacía
        self.historial = []

    def agregar_ejemplar(self):
        nuevo_ejemplar = Ejemplar(id_ejemplar=len(self.ejemplares) + 1)
        self.ejemplares.append(nuevo_ejemplar)
        print(f"Ejemplar agregado con ID {nuevo_ejemplar.id_ejemplar}")

    def cambiar_estado(self, nuevo_estado):
        for ejemplar in self.ejemplares:
            ejemplar.cambiar_estado(nuevo_estado)
        print(f"Estado de todos los ejemplares del artículo '{self.titulo}' cambiado a {nuevo_estado}")
