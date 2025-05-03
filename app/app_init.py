from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialisation des objets de la base de données
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'  # Clé secrète pour gérer les sessions
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'  # URI de la base de données
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Désactive la modification des objets en mémoire

    db.init_app(app)
    migrate = Migrate(app, db)

    from .routes import login, quiz, result
    app.add_url_rule('/', 'login', login, methods=['GET', 'POST'])
    app.add_url_rule('/quiz', 'quiz', quiz)
    app.add_url_rule('/result', 'result', result)

    return app
