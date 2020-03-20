from flask import Response, make_response, jsonify
from sqlalchemy import exc
from manager import db
from datetime import datetime
import hashlib

import json
class Usuario():
    def __init__(self,
                 nome,
                 email,
                 senha,
                 tipoUsuario,
                 dataCriacao,
                 codConfirmacao,
                 pontos,
                 usuario_projeto,
                 usuario_tarefa):

        self.hashCode = str(datetime.timestamp(
            datetime.now())).split('.')

        self.nome = nome
        self.email = email
        self.senha = hashlib.md5(senha)
        self.tipoUsuario = 0
        self.dataCriacao = datetime.now()
        self.codConfirmacao = self.hashCode
        self.pontos = pontos

    def create(email, nome, senha):
        user = Usuario(email, nome, senha)
        try:
            db.session.add(user)
            db.session.commit()
            return True
        except exc.SQLAlchemyError as e:
            return jsonify({'error': f'Erro banco de dados: [{e.args}]'})
        except AttributeError as e1:
            return jsonify({'error:'f'Erro de atributo, valor nulo ou incompativel: [{e1}]'})
