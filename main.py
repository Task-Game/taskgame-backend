from flask import Flask, render_template


app = Flask(__name__)

@app.route("taskgame/api/usuario/login/<int: id>")
def login(id=id):
    user = ModalUser()
    if user.login(id) == True:
        return response = { "login": True }, 200
    else:
        return response = { "login": False }, 201
