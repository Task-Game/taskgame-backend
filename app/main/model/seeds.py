from app.main.model.secondary_tables import RaridadeTable, FrequenciaTable
from ..create_app import db
from sqlalchemy import insert

SEED_DATA_FREQUENCIA = [
    {
        'idFrequencia': 1,
        'descricao': 'Unico'
    },
    {
        'idFrequencia': 2,
        'descricao': 'Diario'
    },
    {
        'idFrequencia': 3,
        'descricao': 'Semanal'
    },
    {
        'idFrequencia': 4,
        'descricao': 'Quinzenal'
    },
    {
        'idFrequencia': 5,
        'descricao': 'Mensal'
    }
]

SEED_DATA_RARIDADE = [
    {
        'idRaridade': 1,
        'descricao': 'Comum',
        'recompensa': 50
    },
    {
        'idRaridade': 2,
        'descricao': 'Incomum',
        'recompensa': 150
    },
    {
        'idRaridade': 3,
        'descricao': 'Raro',
        'recompensa': 300
    },
    {
        'idRaridade': 4,
        'descricao': 'Épico',
        'recompensa': 500
    },
    {
        'idRaridade': 5,
        'descricao': 'Lendario',
        'recompensa': 1000
    },

]


def make_seed():
    db.session.insert(FrequenciaTable).values(SEED_DATA_FREQUENCIA)
    db.session.insert(RaridadeTable).values(SEED_DATA_RARIDADE)

