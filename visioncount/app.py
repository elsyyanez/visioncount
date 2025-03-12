import web  # Carga la librería web.py
from controllers.index import Index
from controllers.usuario import Usuario
from controllers.inicio_sesion import InicioSesion
from controllers.bienvenida_admin import BienvenidaAdmin

urls = (
    '/', 'Index',
    '/usuario', 'Usuario',
    '/inicio_sesion', 'InicioSesion',
    'administrador/bienvenida_admin', 'BienvenidaAdmin',
    '/static/(.*)', 'Static',
)

class Static:
    def GET(self, filename):
        return web.seeother(f'/static/{filename}') 


app = web.application(urls, globals())

if __name__ == "__main__":
    try:
        app.run()
    except Exception as error:
        print(f"ERROR: {str(error)}")