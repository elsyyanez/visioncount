import web

render = web.template.render('views/')

class Usuario:
    def GET(self):
        try: 
            return render.usuario()  # Asegúrate de que usuario.html existe
        except Exception as error:
            message = {
                "error": error.args[0] }
            print(f"ERROR: {message}")
            return message