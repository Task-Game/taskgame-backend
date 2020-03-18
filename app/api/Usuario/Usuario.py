from flask import Response, make_response, jsonify
from manager import db
from datetime import datetime
import hashlib

import json


class Usuario():
    def __init__(self):
        self.hashCode = str(datetime.datetime.timestamp(
            datetime.datetime.now())).split('.')

    def authenticated_login(email, senha):
        if email == 'teste' and senha == 'teste':
            response = {'Aproves': True}
            return make_response(jsonify(response))

    def create(email, nome, senha):
