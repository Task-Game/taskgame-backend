from .. import db, flask_bcrypt


class User(db.Model):
    """
        Classe responavel  pelos dados da entidade usuario
    """

    __tablename__ = "Usuario"

    idUsuario = db.Column(db.Integer,
                          primary_key=True)

    nome = db.Column(db.String(80),
                     unique=True,
                     nullable=False)

    email = db.Column(db.String(60),
                      unique=True,
                      nullable=False)

    dataCriacao = db.Column(db.DateTime,
                            unique=False,
                            nullable=False,
                            default=datetime.datetime.now())

    codigoConfirmacao = db.Column(db.String(50),
                                  unique=False,
                                  nullable=False)

    senha = db.Column(db.String(250),
                      unique=False,
                      nullable=False)

    credito = db.Column(db.Integer,
                        unique=False,
                        nullable=True)

    usuario_projeto = db.relationship(
        'usuario_projeto', backref="usuario_projeto")

    usuario_tarefa = db.relationship(
        'usuario_tarefa', backref="usuario_tarefa")
