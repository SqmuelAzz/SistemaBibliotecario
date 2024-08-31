# controllers/user_controller.py

from models.usuario import Usuario

class UserController:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, usuario):
        if isinstance(usuario, Usuario):
            usuario.registrar()
            self.usuarios.append(usuario)
            print(f"Usuario {usuario.nombre_completo} registrado.")

    def validar_usuario(self, usuario):
        if isinstance(usuario, Usuario):
            usuario.validar_datos()
            print(f"Usuario {usuario.nombre_completo} validado.")
