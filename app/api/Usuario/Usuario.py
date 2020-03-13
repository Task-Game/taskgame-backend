import json
from flask import Response, make_response
# import models
class Usuario():
    def __init__(self):
        pass


    def authenticated_login(email, senha):
        if email == 'teste' and senha == 'teste':
            response  = {'Aproves':True}
            return make_response(json.dumps(response)), 200

    def index():
        pass

            