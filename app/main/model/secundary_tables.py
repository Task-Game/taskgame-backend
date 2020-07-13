from ..create_app import db


class FrequenciaTable(db.Model):
    __tablename__ = "Frequencia"

    idFrequencia = db.Column(db.Integer,
                             primary_key=True)

    descricao = db.Column(db.String(50),
                          nullable=False)

    # A chave desta tabela esta na que se refere
    tarefa = db.relationship('Tarefa', backref="frequencia")



class RaridadeTable(db.Model):
    __tablename__ = 'Raridade'

    idRaridade = db.Column(db.Integer,
                           primary_key=True)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False)

    recompensa = db.Column(db.Integer,
                           unique=False,
                           nullable=False,
                           index=True)

    # O id raridade esta na tabela tarefa
    tarefa = db.relationship('Tarefa', backref="raridade")
    # O id raridade esta na tabela item
    item = db.relationship('Item', backref="raridade")

class ChecklistTable(db.Model):
    __tablename__ = 'Checklist'

    idChecklist = db.Column(db.Integer,
                            primary_key=True)

    Tarefa_idTarefa = db.Column(db.Integer,
                                # A chave de tarefa esta aqui
                                db.ForeignKey('Tarefa.idTarefa'),
                                nullable=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False)

    feito = db.Column(db.Boolean,
                      unique=False,
                      nullable=False)


    def check_token(self):
        return feito



usuario_grupo = db.Table('usuario_grupo',
                         db.Column('idUsuarioGrupo', db.Integer,
                                   primary_key=True),
                         db.Column('Usuario_idUsuario', db.Integer,
                                   db.ForeignKey('Usuario.idUsuario')),

                         db.Column('Grupo_idGrupo', db.Integer,
                                   db.ForeignKey('Grupo.idGrupo'))

                         )

usuario_tarefa = db.Table('usuario_tarefa',
                          db.Column('idUsuarioTarefa', db.Integer,
                                    primary_key=True),
                          db.Column('Usuario_idUsuario', db.Integer,
                                    db.ForeignKey('Usuario.idUsuario')),
                          db.Column('Tarefa_idTarefa', db.Integer,
                                    db.ForeignKey('Tarefa.idTarefa')))
