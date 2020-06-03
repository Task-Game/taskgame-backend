from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
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
    ENV = getenv('ENV')

    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

class TestingConfig(BaseConfig):
    """
    Configuracão ovltada para execucão dos testes, 
    """

    DEBUG = getenv('PORT')
    TESTING = getenv('TESTING')

    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    PRESERVE_CONTEXT_ON_EXCEPTION = getenv('PRESERVE_CONTEXT_ON_EXCEPTION')
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

# Por enquanto só temos a configuração de desenvolvimento.
# Se tiver a de produão tem q colocar aqui tbm

config_by_name = dict(
    dev=Development,
    testing=TestingConfig,
)
