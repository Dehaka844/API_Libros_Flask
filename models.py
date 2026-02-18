# app/models.py
# Definición de los modelos de la base de datos.

from .db import db

class Book(db.Model):
    """
    Modelo de datos para la tabla 'book'.
    Representa un libro con su id, título, autor y año de publicación.
    """
    __tablename__ = 'book' # Nombre explícito de la tabla

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    year_published = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        """
        Convierte el objeto Book en un diccionario para poder serializarlo a JSON.
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year_published': self.year_published
        }
