from flask import Blueprint, request, jsonify
from negocio import UsuarioRN

usuario_controller = Blueprint("usuario_controller", __name__)
usuario_rn = UsuarioRN()   # RN que funciona como DAO


# -----------------------------------------------------------
# FRONT chama isso aqui -> Controller chama a RN
# -----------------------------------------------------------
@usuario_controller.route("/usuario/cadastrar", methods=["POST"])
def cadastrar_usuario():
    dados = request.json

    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    # validação básica
    if not nome or not email or not senha:
        return jsonify({"erro": "Preencha todos os campos."}), 400

    # chama a RN
    resultado = usuario_rn.cadastrar(nome, email, senha)

    if resultado["status"] == "ok":
        return jsonify(resultado), 201
    else:
        return jsonify(resultado), 400
    
@usuario_controller.route("/usuario/login", methods=["POST"])
def login_usuario():
    dados = request.json

    email = dados.get("email")
    senha = dados.get("senha")

    if not email or not senha:
        return jsonify({"erro": "Preencha todos os campos."}), 400

    resultado = usuario_rn.login(email, senha)

    if resultado["status"] == "ok":
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 401
