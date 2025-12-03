from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint("main", __name__)

# Redireciona a rota raiz para cadastro
@main.route("/")
def home():
    return redirect(url_for("main.cadastro"))

# Página de cadastro → cadastro.html
@main.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

# Página inicial → index.html
@main.route("/index")
def index():
    return render_template("index.html")

# Página de login → login.html
@main.route("/login")
def login():
    return render_template("login.html")

# Página de planos → planos.html
@main.route("/planos")
def planos():
    return render_template("planos.html")

# Página de chat → chat.html
@main.route("/chat")
def chat():
    return render_template("chat.html")
