import web  # Carga la librería web.py
import json
import pyrebase  # Asegúrate de que esta librería esté instalada

# Importar controladores
from controllers.index import Index
from controllers.usuario import Usuario
from controllers.inicio_sesion import InicioSesion
from controllers.bienvenida_admin import BienvenidaAdmin

# Configuración de Firebase
firebase_config = {
    "apiKey": "AIzaSyAG9HlMWoXjUC7ub5Dp7OvZnSyPL8nrb1g",
    "authDomain": "integradora-2-51f86.firebaseapp.com",
    "projectId": "integradora-2-51f86",
    "storageBucket": "integradora-2-51f86.appspot.com",
    "messagingSenderId": "752846426914",
    "appId": "1:752846426914:web:6f0915c872335e5678cb7b",
    "databaseURL": "https://integradora-2-51f86-default-rtdb.firebaseio.com/"
}

# Inicializar Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Definir rutas
urls = (
    '/', 'Index',
    '/usuario', 'Usuario',
    '/inicio_sesion', 'InicioSesion',
    '/administrador/bienvenida_admin', 'BienvenidaAdmin',
    '/login', 'Login',
    "/static/js/(.*)", "StaticFileHandler",
    "/static/(.*)", "Static",
)

class Static:
    def GET(self, filename):
        try:
            with open(f"static/{filename}", "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return web.notfound("Archivo no encontrado")

class StaticFileHandler:
    def GET(self, file):
        try:
            with open(f"static/js/{file}", "r", encoding="utf-8") as f:
                web.header("Cache-Control", "no-cache, no-store, must-revalidate")
                web.header("Pragma", "no-cache")
                web.header("Expires", "0")
                return f.read()
        except FileNotFoundError:
            return web.notfound("Archivo JavaScript no encontrado")

class Login:
    def POST(self):
        try:
            data = web.input()
            email = getattr(data, "email", "").strip()
            password = getattr(data, "password", "").strip()

            if not email or not password:
                return json.dumps({"status": "error", "message": "Faltan datos"})

            # Intentar autenticación con Firebase
            user = auth.sign_in_with_email_and_password(email, password)
            return json.dumps({"status": "success", "redirect": "/administrador/bienvenida_admin"})
        except Exception as e:
            print(f"Error en inicio de sesión: {e}")
            return json.dumps({"status": "error", "message": "Datos incorrectos"})

# Iniciar aplicación
app = web.application(urls, globals())

if __name__ == "__main__":
    try:
        app.run()
    except Exception as error:
        print(f"ERROR: {str(error)}")
