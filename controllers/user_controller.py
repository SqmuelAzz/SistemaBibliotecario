# controllers/user_controller.py

from models.usuario import Usuario

class UserController:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def añadir_usuario(self, usuario):
        if not self.biblioteca.es_documento_unico(usuario.documento):
            raise ValueError("Documento de identidad ya registrado")
        if not usuario.validar_correo() or not usuario.validar_telefono():
            raise ValueError("Correo o teléfono inválido")
        self.biblioteca.usuarios.append(usuario)
        return usuario
