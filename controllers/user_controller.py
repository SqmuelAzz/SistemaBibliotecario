# controllers/user_controller.py

from models.usuario import Usuario

class UserController:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def agregar_usuario(self, usuario):
        try:
            self.biblioteca.gestionar_usuario(usuario)
            print("Usuario agregado exitosamente.")
        except ValueError as e:
            print(f"Error: {e}")

    def consultar_usuario(self, identificacion):
        usuario = self.biblioteca.obtener_usuario(identificacion)
        if usuario:
            print(f"Usuario encontrado: {usuario.nombre_completo}")
        else:
            print("Usuario no encontrado.")

    def listar_usuarios(self):
        usuarios = self.biblioteca.listar_usuarios()
        for usuario in usuarios:
            print(f"{usuario.identificacion}: {usuario.nombre_completo}")
