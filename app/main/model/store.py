from ..create_app import db
from datetime import datetime
from .main_models import *
from .secondary_tables import *


class LojaTable(db.Model):
    __tablename__ = 'Loja'

    idLoja = db.Column(db.Integer,
                       primary_key=True)

    dataAbertura = db.Column(db.DateTime,
                             unique=False,
                             nullable=False,
                             default=datetime.now())

    dataFechamento = db.Column(db.DateTime,
                               unique=False,
                               nullable=False)

    item = db.relationship('ItemTable', backref='loja')
    grupo = db.relationship('GrupoTable', backref='loja')
