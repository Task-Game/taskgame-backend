from flask_sqlalchemy import SQLAlchemy
from app import create_app
from ..manager import db

class User(db.Model):
    """
    Classe model responsavel pelos dados do usuario
    """

    __tablename__ = 'Usuario'
    idUsuario = db.Column(db.Integer,
                          primary_key = True)
    # chave estrangeira estuda mais dps
    # TipoUsuario_idTipoUsuario = db.relationship('TipoUsuario') 
    nome = db.Column(db.String(80),
                      unique=False,
                      nullable=False,
                      index=False)
    
    email = db.Column(db.String(60),
                      unique=True,
                      nullable=False,
                      index=True)
    
    dataNascimento = db.Column(db.DateTime,
                      unique=False,
                      nullable=False,
                      index=False)

    senha = db.Column(String(18),
                      unique=False,
                      nullable=False,
                      index=False)
    
    def __repr__(self):
        return '<Email {}>'.format(self.email)