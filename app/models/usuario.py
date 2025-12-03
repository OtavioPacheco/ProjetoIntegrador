from app import db

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id_usuario = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(100), nullable=False)
    email_usuario = db.Column(db.String(120), unique=True, nullable=False)
    senha_usuario = db.Column(db.String(120), nullable=False)

