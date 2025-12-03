from flask import Flask
from .extensions import db, migrate

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Configurações gerais
    app.config.from_object('config')
    app.config.from_pyfile('config.py', silent=True)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    from .routes import main
    from .controllers.usuario_controller import usuario_controller

    app.register_blueprint(main)
    app.register_blueprint(usuario_controller)

    return app
