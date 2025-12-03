from flask import Blueprint, request, jsonify
from app.negocio.usuario_rn import UsuarioRN

usuario_controller = Blueprint("usuario_controller", __name__)
usuario_rn = UsuarioRN()   # Agora não precisa de conexão


# -----------------------------------------------------------
# CADASTRAR USUÁRIO
# -----------------------------------------------------------
@usuario_controller.route("/usuario/cadastrar", methods=["POST"])
def cadastrar_usuario():
    dados = request.get_json()
    print("Dados recebidos:", dados)


    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    if not nome or not email or not senha:
        return jsonify({
            "status": "erro",
            "mensagem": "Preencha todos os campos."
        }), 400

    # chama a RN
    resultado = usuario_rn.cadastrar(nome, email, senha)

    status = 201 if resultado["status"] == "ok" else 400
    return jsonify(resultado), status


# -----------------------------------------------------------
# LOGIN
# -----------------------------------------------------------
@usuario_controller.route("/usuario/login", methods=["POST"])
def login_usuario():
    dados = request.json or {}

    email = dados.get("email")
    senha = dados.get("senha")

    if not email or not senha:
        return jsonify({
            "status": "erro",
            "mensagem": "Preencha todos os campos."
        }), 400

    resultado = usuario_rn.login(email, senha)

    status = 200 if resultado["status"] == "ok" else 401
    return jsonify(resultado), status
