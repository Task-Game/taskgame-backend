from ..create_app import db


class LojaTable(db.Model):
    __tablename__ = 'Loja'

    idLoja = db.Column(db.Integer,
                       primary_key=True)

    dataAbertura = db.Column(db.DateTime,
                             unique=False,
                             nullable=False,
                             default=datetime.datetime.now())

    dataFechamento = db.Column(db.DateTime,
                               unique=False,
                               nullable=False)

    item = db.relationship('Item', backref='loja')
    grupo = db.relationship('Grupo', backref='loja')


