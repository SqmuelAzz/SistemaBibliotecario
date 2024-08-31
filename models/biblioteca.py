# models/biblioteca.py

from singleton_decorator import singleton
from models.usuario import Usuario
from models.articulo import Articulo
from models.prestamo import Prestamo
from models.multa import Multa

@singleton
class Biblioteca:
    def __init__(self):
        self.usuarios = {}
        self.articulos = []
        self.prestamos = []
        self.multas = []

    def gestionar_usuario(self, usuario):
        if isinstance(usuario, Usuario):
            if usuario.identificacion in self.usuarios:
                raise ValueError("El usuario ya existe.")
            self.usuarios[usuario.identificacion] = usuario
            usuario.registrar()
            print(f"Usuario {usuario.nombre_completo} gestionado.")
        else:
            raise TypeError("El objeto debe ser una instancia de Usuario.")

    def obtener_usuario(self, identificacion):
        return self.usuarios.get(identificacion, None)
    
    def listar_usuarios(self):
        return list(self.usuarios.values())

    def gestionar_prestamo(self, prestamo):
        if isinstance(prestamo, Prestamo):
            self.prestamos.append(prestamo)
            prestamo.registrar_prestamo()
            print(f"Préstamo {prestamo.id_prestamo} gestionado.")
        else:
            raise TypeError("El objeto debe ser una instancia de Prestamo.")

    def gestionar_articulo(self, articulo):
        if isinstance(articulo, Articulo):
            self.articulos.append(articulo)
            print(f"Artículo {articulo.titulo} gestionado.")
        else:
            raise TypeError("El objeto debe ser una instancia de Articulo.")

    def gestionar_multa(self, multa):
        if isinstance(multa, Multa):
            self.multas.append(multa)
            multa.aplicar_multa()
            print(f"Multa {multa.id_multa} gestionada.")
        else:
            raise TypeError("El objeto debe ser una instancia de Multa.")
