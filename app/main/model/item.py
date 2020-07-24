from ..create_app import db


class ItemTable(db.Model):
    __tablename__ = 'Item'

    idItem = db.Column(db.Integer,
                       primary_key=True)

    Loja_idLoja = db.Column(db.Integer,
                            db.ForeignKey('Loja.idLoja'))

    nome = db.Column(db.String(50),
                     nullable=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False)

    valor = db.Column(db.Integer,
                      unique=False,
                      nullable=False)
