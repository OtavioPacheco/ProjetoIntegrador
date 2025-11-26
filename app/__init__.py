from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True
    )

    # Configurações gerais (config.py na raiz)
    app.config.from_object('config')

    # Configurações privadas (instance/config.py)
    app.config.from_pyfile('config.py', silent=True)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Rotas / Blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
