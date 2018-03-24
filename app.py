from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Server, Manager
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from ledstrip import ledstrip

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
leds = ledstrip()

server = Server(host="0.0.0.0", port=5000)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", server)