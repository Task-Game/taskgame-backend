from .. import db, flask_bcrypt
import  hashlib


class User(db.Model):
    """
    Classe model responsavel pelos dados do usuario
    """

    __tablename__ = 'Usuario'

    idUsuario = db.Column(db.Integer,
                          primary_key=True)

    nome = db.Column(db.String(80), unique=False, nullable=False)

    email = db.Column(db.String(60), unique=True, nullable=False)

    cargo = db.Column(db.String(50), unique=False, nullable=True)

    dataCriacao = db.Column(db.DateTime, unique=False, nullable=False,
                            default=datetime.datetime.now())

    codigoConfirmacao = db.Column(db.String(50), unique=False, nullable=False)

    senha = db.Column(db.String(250), unique=False, nullable=False)

    credito = db.Column(db.Integer, unique=False, nullable=True,)

    usuario_grupo = db.relationship(
        'usuario_grupo', backref="usuario")

    usuario_tarefa = db.relationship(
        'usuario_tarefa', backref="usuario")
    

    @property
    def senha(self):
        raise AttributeError('senha: write-only fild')
    
    @senha.setter
    def senha(self, senha):
        self.senha = flask_bcrypt.generate_password_hash(senha).decode('utf-8')

    def check_senha(self, senha):
        return flask_bcrypt.check_password_hash(self.senha, senhas)

    def __repr__(self):
        return f"<User '{self.nome}'>"