from __init__ import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

app = create_app()

db = SQLAlchemy(app)

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

import app.database

if __name__ == "__main__":
    manager.run()
