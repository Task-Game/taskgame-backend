class BaseConfig(object):
    """
    Classe de configuração basica, esses atributos vão
    ser usados por produção e desenvolvimento
    """

    ORIGINS = ["*"] # Para chamadas da API
    SECRET_KEY = "xDxD" # Chave de validação

class Development(BaseConfig):
    """
    Configurações de desenvolvimento. Usaremos o modo Debug
    Modo debub = Para mais informações leia a documentação
    """
    PORT = 5000
    DEBUG = True
    TESTING = False
    ENV = 'dev'

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