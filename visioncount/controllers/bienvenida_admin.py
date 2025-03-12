import web

render = web.template.render('views/administrador')

class BienvenidaAdmin:
    def GET(self):
        try:
            return render.bienvenida_admin()  # Asegúrate de que `bienvenida_admin.html` exista
        except Exception as error:
            message = {"error": str(error)}  # Mostrar el mensaje de error de forma más legible
            print(f"ERROR: {message}")
            return f"Hubo un error: {message['error']}"  # Devuelve un mensaje de error al usuario
