from os import environ

class BaseConfig(object):
    """
    Classe de configuração basica, esses atributos vão
    ser usados por produção e desenvolvimento
    """

    ORIGINS = environ.get('ORIGINS') # Para chamadas da API
    SECRET_KEY = environ.get('SECRET_KEY') # Chave de validação

class Development(BaseConfig):
    """
    Configurações de desenvolvimento. Usaremos o modo Debug
    Modo debub = Para mais informações leia a documentação
    """
    PORT = environ.get('PORT')
    DEBUG = environ.get('DEBUG')
    TESTING = environ.get('TESTING')
    ENV = environ.get('ENV')

    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')



# Por enquanto só temos a configuração de desenvolvimento.
# Se tiver a de produão tem q colocar aqui tbm
config = {
    'development':'config.Development'
}

def configure_app(app):
    """
    As configurações do app serão feitas aqui

    Parametros
    ------------

    app: Instancia do App flask
    """

    app.config.from_object(config['development'])