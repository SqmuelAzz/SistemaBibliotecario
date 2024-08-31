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
        console.print("4. Generar Reportes")
        console.print("5. Salir")

        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4", "5"])

        if opcion == "1":
            gestionar_usuarios()
        elif opcion == "2":
            gestionar_catalogo()
        elif opcion == "3":
            gestionar_prestamos()
        elif opcion == "4":
            generar_reportes()
        elif opcion == "5":
            console.print("¡Hasta luego!", style="bold green")
            break

def gestionar_usuarios():
    while True:
        console.print(Panel("Gestión de Usuarios", title="Usuarios"))
        console.print("1. Agregar Usuario")
        console.print("2. Consultar Usuario")
        console.print("3. Listar Usuarios")
        console.print("4. Volver al Menú Principal")

        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4"])

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            consultar_usuario()
        elif opcion == "3":
            listar_usuarios()
        elif opcion == "4":
            break

def agregar_usuario():
    identificacion = input("Ingrese la identificación del usuario: ")
    nombre = input("Ingrese el nombre completo del usuario: ")
    direccion = input("Ingrese la dirección del usuario: ")
    celular = input("Ingrese el número de celular del usuario: ")
    correo = input("Ingrese el correo electrónico del usuario: ")
    
    fecha_nacimiento_str = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
    
    ocupacion = input("Ingrese la ocupación del usuario: ")
    centro_estudio = input("Ingrese el centro de estudio del usuario: ")

    usuario = Usuario(identificacion=identificacion, nombre_completo=nombre, direccion=direccion, 
                      celular=celular, correo=correo, fecha_nacimiento=fecha_nacimiento, 
                      ocupacion=ocupacion, centro_estudio=centro_estudio)
    
    usuario.validar_datos()
    biblioteca = Biblioteca()  # Obtén la instancia de la biblioteca (Singleton)
    user_controller = UserController(biblioteca)
    user_controller.agregar_usuario(usuario)

def consultar_usuario():
    identificacion = input("Ingrese la identificación del usuario a consultar: ")
    biblioteca = Biblioteca()  # Obtén la instancia de la biblioteca (Singleton)
    user_controller = UserController(biblioteca)
    user_controller.consultar_usuario(identificacion)

def listar_usuarios():
    biblioteca = Biblioteca()  # Obtén la instancia de la biblioteca (Singleton)
    user_controller = UserController(biblioteca)
    user_controller.listar_usuarios()

def gestionar_catalogo():
    console.print(Panel("Gestión de Catálogo", title="Catálogo"))
    id_articulo = Prompt.ask("Ingrese el ID del artículo")
    titulo = Prompt.ask("Ingrese el título del artículo")
    autor = Prompt.ask("Ingrese el autor del artículo")
    ano_publicacion = Prompt.ask("Ingrese el año de publicación del artículo")
    editorial = Prompt.ask("Ingrese la editorial del artículo")
    categoria = Prompt.ask("Ingrese la categoría del artículo")
    palabras_clave = Prompt.ask("Ingrese las palabras clave del artículo (separadas por comas)")
    cantidad = Prompt.ask("Ingrese la cantidad de ejemplares")

    articulo = Articulo(id_articulo=id_articulo, titulo=titulo, autor=autor, ano_publicacion=ano_publicacion, 
                        editorial=editorial, categoria=categoria, palabras_clave=palabras_clave.split(','), 
                        cantidad=int(cantidad))
    
    # Aquí puedes manejar la lógica de guardar el artículo en el catálogo.
    console.print(f"Artículo '{articulo.titulo}' agregado exitosamente.", style="bold green")

def gestionar_prestamos():
    console.print(Panel("Gestión de Préstamos", title="Préstamos"))
    usuario_id = Prompt.ask("Ingrese el ID del usuario")
    articulo_id = Prompt.ask("Ingrese el ID del artículo")

    # Aquí debes hacer la lógica para manejar el préstamo y guardarlo.
    console.print(f"Préstamo registrado exitosamente para el usuario {usuario_id} y el artículo {articulo_id}.", style="bold green")

def generar_reportes():
    console.print(Panel("Generar Reportes", title="Reportes"))
    console.print("1. Artículos Más Prestados")
    console.print("2. Usuarios Que Más Utilizan La Biblioteca")
    console.print("3. Artículos Perdidos")
    console.print("4. Artículos Dañados")
    console.print("5. Ingresos Por Multas")
    console.print("6. Por Categoría")
    console.print("7. Rango De Fechas")
    console.print("8. Exportar en Excel")
    console.print("9. Exportar en PDF")
    console.print("10. Reportes Semanales")
    console.print("11. Reportes Mensuales")

    opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])

    if opcion == "1":
        reportes_articulos_mas_prestados()
    elif opcion == "2":
        reportes_usuarios_mas_utilizan()
    elif opcion == "3":
        reportes_articulos_perdidos()
    elif opcion == "4":
        reportes_articulos_danados()
    elif opcion == "5":
        reportes_ingresos_multas()
    elif opcion == "6":
        reportes_por_categoria()
    elif opcion == "7":
        reportes_rango_fechas()
    elif opcion == "8":
        exportar_excel()
    elif opcion == "9":
        exportar_pdf()
    elif opcion == "10":
        reportes_semanales()
    elif opcion == "11":
        reportes_mensuales()

def reportes_articulos_mas_prestados():
    # Implementa la lógica para generar el reporte de artículos más prestados
    console.print("Reporte: Artículos Más Prestados")

def reportes_usuarios_mas_utilizan():
    # Implementa la lógica para generar el reporte de usuarios que más utilizan la biblioteca
    console.print("Reporte: Usuarios Que Más Utilizan La Biblioteca")

def reportes_articulos_perdidos():
    # Implementa la lógica para generar el reporte de artículos perdidos
    console.print("Reporte: Artículos Perdidos")

def reportes_articulos_danados():
    # Implementa la lógica para generar el reporte de artículos dañados
    console.print("Reporte: Artículos Dañados")

def reportes_ingresos_multas():
    # Implementa la lógica para generar el reporte de ingresos por multas
    console.print("Reporte: Ingresos Por Multas")

def reportes_por_categoria():
    # Implementa la lógica para generar el reporte por categoría
    console.print("Reporte: Por Categoría")

def reportes_rango_fechas():
    # Implementa la lógica para generar el reporte por rango de fechas
    console.print("Reporte: Rango De Fechas")

def exportar_excel():
    # Implementa la lógica para exportar los reportes en formato Excel
    console.print("Exportar Reporte en Excel")

def exportar_pdf():
    # Implementa la lógica para exportar los reportes en formato PDF
    console.print("Exportar Reporte en PDF")

def reportes_semanales():
    # Implementa la lógica para generar reportes semanales
    console.print("Reporte Semanal")

def reportes_mensuales():
    # Implementa la lógica para generar reportes mensuales
    console.print("Reporte Mensual")

if __name__ == "__main__":
    main()
