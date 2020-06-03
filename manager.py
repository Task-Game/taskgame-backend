import unittest

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.main.create_app import create_app, db

app = create_app('dev')
app.app_context().push()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


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
