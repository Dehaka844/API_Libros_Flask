# app/routes.py
# Definición de las rutas (endpoints) de la API.

from flask import Blueprint, request, jsonify
from .models import Book
from .db import db

# Creamos un Blueprint. Es como una mini-aplicación para agrupar rutas.
api_bp = Blueprint('api', __name__)

# --- Endpoint para OBTENER todos los libros (GET) y CREAR un libro (POST) ---
@api_bp.route('/books', methods=['GET', 'POST'])
def handle_books():
    """
    Maneja las peticiones a /api/books.
    - GET: Devuelve una lista de todos los libros.
    - POST: Crea un nuevo libro.
    """
    if request.method == 'GET':
        books = Book.query.all()
        # Convertimos cada objeto libro a un diccionario y lo metemos en una lista
        books_list = [book.to_dict() for book in books]
        return jsonify(books_list), 200

    if request.method == 'POST':
        # Obtenemos los datos JSON enviados en la petición
        data = request.get_json()
        if not data or not 'title' in data or not 'author' in data:
            return jsonify({'error': 'Missing data. Title and author are required.'}), 400

        # Creamos una nueva instancia del modelo Book
        new_book = Book(
            title=data['title'],
            author=data['author'],
            year_published=data.get('year_published') # .get() para campos opcionales
        )

        # Añadimos el nuevo libro a la sesión de la base de datos y guardamos
        db.session.add(new_book)
        db.session.commit()

        return jsonify(new_book.to_dict()), 201 # 201 Created

# --- Endpoints para OBTENER, ACTUALIZAR y BORRAR un libro específico por su ID ---
@api_bp.route('/books/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(book_id):
    """
    Maneja las peticiones a /api/books/<id>.
    - GET: Devuelve un libro específico.
    - PUT: Actualiza un libro específico.
    - DELETE: Borra un libro específico.
    """
    # Buscamos el libro en la BD. .first_or_404() devuelve el libro o un error 404 si no lo encuentra.
    book = Book.query.get_or_404(book_id)

    if request.method == 'GET':
        return jsonify(book.to_dict()), 200

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing data.'}), 400

        # Actualizamos los campos del libro con los nuevos datos
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.year_published = data.get('year_published', book.year_published)

        db.session.commit()
        return jsonify(book.to_dict()), 200

    if request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        # No se devuelve contenido, solo una confirmación de que se ha borrado.
        return '', 204 # 204 No Content
