import os

SECRET_KEY = "minha-chave"

# Configuração MySQL
MYSQL_USER = "root"
MYSQL_PASSWORD = "1234"
MYSQL_HOST = "localhost"
MYSQL_DB = "meu_banco"

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
