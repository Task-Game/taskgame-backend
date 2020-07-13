from ..create_app import db


class TarefaTable(db.Model):
    __tablename__ = 'Tarefa'

    idTarefa = db.Column(db.Integer,
                         primary_key=True)

    Grupo_idGrupo = db.Column(db.Integer,
                              db.ForeignKey('Grupo.idGrupo'),
                              nullable=True)

    Raridade_idRaridade = db.Column(db.Integer,
                                    db.ForeignKey('Raridade.idRaridade'))

    Frequencia_idFrequencia = db.Column(db.Integer,
                                        db.ForeignKey(
                                            'Frequencia.idFrequencia'),
                                        nullable=True)

    dataAbertura = db.Column(db.DateTime,
                             unique=False,
                             nullable=False,
                             default=datetime.datetime.now())

    nome = db.Column(db.String(100),
                     unique=True,
                     nullable=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False)

    prazo = db.Column(db.DateTime,
                      unique=False,
                      nullable=False)

    recompensa = db.Column(db.Integer,
                           unique=True,
                           nullable=False)

    status = db.Column(db.Boolean,
                       unique=False,
                       nullable=True)

    usuario_tarefa = db.relationship(
        'usuario_tarefa', backref="tarefa")