import unittest

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.main.create_app import create_app, db
from app.main.model import main_models, item, secondary_tables, store
from app.main.model.seeds import make_seed
from app import blueprint


app = create_app('development')
app.register_blueprint(blueprint)
app.app_context().push()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    """
    Roda o app é isso ae
    """
    app.run()


@manager.command
def seed():
    """
    Roda seeds  é trab
    """
    make_seed()

@manager.command
def test():
    """
    Roda os testes unitarios
    """
    tests = unittest.TestLoader().discover('app/test',
                                           pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
