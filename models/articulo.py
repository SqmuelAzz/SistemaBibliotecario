# models/articulo.py

class Ejemplar:
    def __init__(self, id_ejemplar, estado="disponible"):
        self.id_ejemplar = id_ejemplar
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado


class Articulo:
    def __init__(self, id_articulo, titulo, autor, ano_publicacion, editorial, categoria, palabras_clave, cantidad):
        self.id_articulo = id_articulo
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.editorial = editorial
        self.categoria = categoria
        self.palabras_clave = palabras_clave
        self.cantidad = cantidad
        self.ejemplares = [Ejemplar(id_ejemplar=i) for i in range(cantidad)]
        self.historial = []

    def agregar_ejemplar(self):
        nuevo_ejemplar = Ejemplar(id_ejemplar=len(self.ejemplares) + 1)
        self.ejemplares.append(nuevo_ejemplar)
        print(f"Ejemplar agregado con ID {nuevo_ejemplar.id_ejemplar}")

    def cambiar_estado(self, nuevo_estado):
        for ejemplar in self.ejemplares:
            ejemplar.cambiar_estado(nuevo_estado)
        print(f"Estado de todos los ejemplares del artículo '{self.titulo}' cambiado a {nuevo_estado}")
