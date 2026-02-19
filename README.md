# API REST de Libros - Proyecto Demo

Este proyecto es una API RESTful construida con Python y Flask que permite a los usuarios gestionar una colección de libros. Implementa operaciones CRUD (Crear, Leer, Actualizar, Borrar) completas a través de endpoints HTTP.

El propósito de este repositorio es demostrar habilidades en desarrollo backend con Python, incluyendo la creación de APIs, la interacción con bases de datos y la estructuración de un proyecto de manera profesional y escalable.

## Características

*   **Listar todos los libros:** Obtiene una lista completa de los libros en la base de datos.
*   **Obtener un libro:** Recupera los detalles de un libro específico por su ID.
*   **Añadir un nuevo libro:** Crea un nuevo registro de libro.
*   **Actualizar un libro:** Modifica la información de un libro existente.
*   **Eliminar un libro:** Borra un libro de la base de datos.

## Tecnologías Utilizadas

*   **Backend:**
    *   **Python 3:** Lenguaje de programación principal.
    *   **Flask:** Microframework web para construir la API.
    *   **Flask-SQLAlchemy:** Extensión para manejar la base de datos a través del ORM SQLAlchemy.
*   **Base de Datos:**
    *   **SQLite:** Base de datos ligera basada en archivos, ideal para desarrollo y proyectos pequeños.
*   **Estructura del Proyecto:**
    *   **Application Factory Pattern:** Para una inicialización de la aplicación limpia y escalable.
    *   **Blueprints:** Para organizar las rutas de la API de forma modular.

## Instalación y Ejecución

Para ejecutar este proyecto localmente, sigue estos pasos:

**1. Prerrequisitos:**
   *   Tener Python 3.8 o superior instalado.
   *   Tener `pip` (el gestor de paquetes de Python) instalado.

**2. Clonar el Repositorio:**
   ```bash
   git clone https://github.com/Dehaka844/api_libros.git
   cd api_libros
   ```

**3. (Recomendado ) Crear un Entorno Virtual:**
   Un entorno virtual aísla las dependencias de tu proyecto.
   ```bash
   # En Windows
   python -m venv venv
   venv\Scripts\activate

   # En macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

**4. Instalar las Dependencias:**
   El archivo `requirements.txt` contiene todas las librerías necesarias.
   ```bash
   pip install -r requirements.txt
   ```

**5. Ejecutar la Aplicación:**
   Una vez instaladas las dependencias, puedes iniciar el servidor de desarrollo de Flask.
   ```bash
   python run.py
   ```
   La API estará disponible en `http://127.0.0.1:5000`. La primera vez que se ejecute, se creará automáticamente un archivo `books.db` con la base de datos.

## Endpoints de la API

La URL base para todos los endpoints es `/api`.

| Método | Endpoint                | Descripción                                | Body (JSON ) de Ejemplo                               |
|--------|-------------------------|--------------------------------------------|------------------------------------------------------|
| `GET`  | `/books`                | Obtiene la lista de todos los libros.      | N/A                                                  |
| `POST` | `/books`                | Crea un nuevo libro.                       | `{"title": "El Quijote", "author": "Cervantes"}`      |
| `GET`  | `/books/<id>`           | Obtiene un libro por su ID.                | N/A                                                  |
| `PUT`  | `/books/<id>`           | Actualiza un libro existente.              | `{"year_published": 1605}`                           |
| `DELETE`| `/books/<id>`          | Elimina un libro por su ID.                | N/A                                                  |

---
*Desarrollado por David Arenas Cabeza.*
