import os

SECRET_KEY = "minha-chave"

# Configuração MySQL
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_HOST = "localhost"
MYSQL_DB = "portal"

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
