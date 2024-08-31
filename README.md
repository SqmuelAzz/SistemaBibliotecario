# Sistema de Gestión de Biblioteca

## Descripción

Este proyecto es un sistema de gestión de biblioteca desarrollado en Python. Utiliza patrones de diseño como Singleton y Composite para manejar usuarios, artículos, préstamos y multas en una biblioteca. La interfaz de usuario se maneja a través de la biblioteca [Rich](https://github.com/Textualize/rich), que proporciona una experiencia de línea de comandos mejorada con paneles, mensajes y prompts interactivos.

## Características

- **Gestión de Usuarios:** Agregar, consultar y listar usuarios.
- **Gestión de Artículos:** Agregar y gestionar artículos en el catálogo.
- **Gestión de Préstamos:** Registrar préstamos de artículos.
- **Generación de Reportes:** Crear reportes sobre artículos, usuarios y multas, y exportar en diferentes formatos.
- **Interfaz de Usuario:** Utiliza Rich para una interfaz de línea de comandos intuitiva y visualmente atractiva.

## Requerimientos

Para ejecutar este proyecto, necesitas instalar las siguientes dependencias:

- **Rich**: Para la interfaz de usuario enriquecida en la línea de comandos.
- **singleton-decorator**: Para implementar el patrón Singleton en la clase `Biblioteca`.

Puedes instalar estas dependencias utilizando `pip`:

```bash
pip install rich singleton-decorator

Ejecución del Proyecto
Para ejecutar el proyecto, sigue estos pasos:

Clona el repositorio:

bash git clone <(https://github.com/SqmuelAzz/SistemaBibliotecario.git)>
Navega al directorio del proyecto:

bash cd biblioteca
Instala las dependencias:

bash pip install -r requirements.txt
Ejecuta la aplicación:

bash python main.py
