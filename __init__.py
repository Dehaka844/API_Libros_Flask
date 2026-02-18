# app/__init__.py
# Fábrica de la aplicación Flask.

from flask import Flask
from .db import db
from .routes import api_bp

def create_app():
    """
    Fábrica de creación de la aplicación Flask.
    Configura la aplicación, inicializa la base de datos y registra las rutas.
    """
    app = Flask(__name__)

    # --- Configuración de la Aplicación ---
    # La URI de la base de datos. En este caso, un archivo 'books.db' en la raíz del proyecto.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    # Desactiva una característica de seguimiento de modificaciones que no necesitamos.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- Inicialización de Extensiones ---
    # Inicializa SQLAlchemy con la configuración de la aplicación.
    db.init_app(app)

    # --- Registro de Blueprints (Rutas) ---
    # Un Blueprint es un conjunto de rutas. Esto nos permite organizar el código.
    app.register_blueprint(api_bp, url_prefix='/api')

    # --- Creación de la Base de Datos ---
    # Este contexto es necesario para que SQLAlchemy sepa a qué aplicación pertenece la BD.
    with app.app_context():
        # Crea todas las tablas definidas en los modelos si no existen.
        db.create_all()

    return app
