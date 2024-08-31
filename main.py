from models.biblioteca import Biblioteca
from models.usuario import Usuario
from models.articulo import Articulo
from models.prestamo import Prestamo
from models.multa import Multa
from controllers.user_controller import UserController
from controllers.catalog_controller import CatalogController
from controllers.loan_controller import LoanController
from views.user_view import UserView
from views.catalog_view import CatalogView
from views.loan_view import LoanView
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from datetime import datetime  # Importar datetime

console = Console()

def main():
    # Inicialización de la Biblioteca (Singleton)
    biblioteca = Biblioteca()

    # Menú principal
    while True:
        console.print(Panel("Bienvenido a la Biblioteca", title="Sistema de Gestión de Biblioteca"))
        console.print("1. Gestionar Usuarios")
        console.print("2. Gestionar Catálogo")
        console.print("3. Gestionar Préstamos")
        console.print("4. Salir")

        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4"])

        if opcion == "1":
            gestionar_usuarios()
        elif opcion == "2":
            gestionar_catalogo()
        elif opcion == "3":
            gestionar_prestamos()
        elif opcion == "4":
            console.print("¡Hasta luego!", style="bold green")
            break

def gestionar_usuarios():
    # Ingresar datos del usuario
    identificacion = input("Ingrese la identificación del usuario: ")
    nombre = input("Ingrese el nombre completo del usuario: ")
    direccion = input("Ingrese la dirección del usuario: ")
    celular = input("Ingrese el número de celular del usuario: ")
    correo = input("Ingrese el correo electrónico del usuario: ")
    
    # Convertir la fecha de nacimiento a datetime
    fecha_nacimiento_str = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
    
    ocupacion = input("Ingrese la ocupación del usuario: ")
    centro_estudio = input("Ingrese el centro de estudio del usuario: ")

    # Crear la instancia del usuario
    usuario = Usuario(identificacion=identificacion, nombre_completo=nombre, direccion=direccion, 
                      celular=celular, correo=correo, fecha_nacimiento=fecha_nacimiento, 
                      ocupacion=ocupacion, centro_estudio=centro_estudio)
    
    usuario.registrar()
    usuario.validar_datos()

def gestionar_catalogo():
    console.print(Panel("Gestión de Catálogo", title="Catálogo"))
    titulo = Prompt.ask("Ingrese el título del artículo")
    autor = Prompt.ask("Ingrese el autor del artículo")
    editorial = Prompt.ask("Ingrese la editorial del artículo")
    isbn = Prompt.ask("Ingrese el ISBN del artículo")

    articulo = Articulo(titulo=titulo, autor=autor, editorial=editorial, isbn=isbn)
    
    # Aquí puedes manejar la lógica de guardar el artículo en el catálogo.
    console.print(f"Artículo '{articulo.titulo}' agregado exitosamente.", style="bold green")

def gestionar_prestamos():
    console.print(Panel("Gestión de Préstamos", title="Préstamos"))
    # Aquí podrías pedir al usuario seleccionar un usuario y un artículo para hacer el préstamo.
    usuario_id = Prompt.ask("Ingrese el ID del usuario")
    articulo_id = Prompt.ask("Ingrese el ID del artículo")

    # Aquí debes hacer la lógica para manejar el préstamo y guardarlo.
    console.print(f"Préstamo registrado exitosamente para el usuario {usuario_id} y el artículo {articulo_id}.", style="bold green")

if __name__ == "__main__":
    main()
