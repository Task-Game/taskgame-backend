from app.main.model.secondary_tables import RaridadeTable, FrequenciaTable

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
    frequency_unique = FrequenciaTable(
        descricao='Unico'
    ).save()
    frequency_daily = FrequenciaTable(
        descricao='Diario'
    ).save()
    frequency_weekly = FrequenciaTable(
        descricao='Semanal'
    ).save()
    frequency_fortnightly = FrequenciaTable(
        descricao='Quinzenal'
    ).save()
    frequency_monthly = FrequenciaTable(
        descricao='Mensal'
    ).save()

    rarity_comum = RaridadeTable(
        descricao='Comum',
        recompensa=50
    ).save()
    rarity_incomum = RaridadeTable(
        descricao='Incomum',
        recompensa=150
    ).save()
    rarity_rare = RaridadeTable(
        descricao='Raro',
        recompensa=300
    ).save()
    rarity_epic = RaridadeTable(
        descricao='Épico',
        recompensa=500
    ).save()
    rarity_legendary = RaridadeTable(
        descricao='Lendario',
        recompensa=1000
    ).save()
