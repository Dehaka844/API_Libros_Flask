# app/db.py
# Inicialización de la extensión SQLAlchemy.

from flask_sqlalchemy import SQLAlchemy

# Se crea una instancia de SQLAlchemy sin asociarla a ninguna aplicación todavía.
# La asociación se hará en la fábrica de la aplicación.
db = SQLAlchemy()
