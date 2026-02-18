# run.py
# Punto de entrada principal para la aplicación.

from app import create_app

# Llama a la fábrica para crear una instancia de la aplicación
app = create_app()

if __name__ == '__main__':
    # Inicia el servidor de desarrollo de Flask
    # debug=True activa el modo de depuración para ver errores detallados en el navegador
    app.run(debug=True)
