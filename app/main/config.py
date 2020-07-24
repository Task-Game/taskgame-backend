class BaseConfig(object):
    """
    Classe de configuração basica, esses atributos vão
    ser usados por produção e desenvolvimento
    """

    ORIGINS = "*" # Para chamadas da API
    SECRET_KEY = 'eu_amo_de_bts' # Chave de validação

class Development(BaseConfig):
    """
    Configurações de desenvolvimento. Usaremos o modo Debug
    Modo debub = Para mais informações leia a documentação
    """
    PORT = 5050
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:senhasenha@localhost:3306/taskGame'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Testing(BaseConfig):
    """
    Configuracão voltada para execucão dos testes, 
    """

    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:senhasenha@localhost:3306/taskGame'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(BaseConfig):
    DEBUG = False
    
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:senhasenha@locahost:3306/taskGame'



# Por enquanto só temos a configuração de desenvolvimento.
# Se tiver a de produão tem q colocar aqui tbm

config_by_name = {
    'development':Development,
    'testing':Testing,
    'production':Production
}
