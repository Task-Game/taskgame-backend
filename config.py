from dotenv import load_dotenv
load_dotenv()
from os import getenv

class BaseConfig(object):
    """
    Classe de configuração basica, esses atributos vão
    ser usados por produção e desenvolvimento
    """

    ORIGINS = getenv('ORIGINS') # Para chamadas da API
    SECRET_KEY = getenv('SECRET_KEY') # Chave de validação

class Development(BaseConfig):
    """
    Configurações de desenvolvimento. Usaremos o modo Debug
    Modo debub = Para mais informações leia a documentação
    """
    PORT = getenv('PORT')
    DEBUG = getenv('DEBUG')
    TESTING = getenv('TESTING')
    ENV = getenv('ENV')

    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')



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