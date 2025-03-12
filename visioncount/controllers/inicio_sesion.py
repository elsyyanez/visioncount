import web

render = web.template.render('views/')

class InicioSesion:
    def GET(self):
        try: 
            return render.inicio_sesion()  # Asegúrate de que usuario.html existe
        except Exception as error:
            message = {
                "error": error.args[0] }
            print(f"ERROR: {message}")
            return message