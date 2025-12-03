from app.models.usuario import Usuario
from app import db

class UsuarioRN:

    # ----------------------------------------------------------
    # CADASTRAR USUÁRIO
    # ----------------------------------------------------------

    def cadastrar(self, nome, email, senha):
        usuario = Usuario.query.filter_by(email_usuario=email).first()
        print("Dados recebidos:", nome , email ,senha)

        if usuario:
            return {"status": "erro", "mensagem": "E-mail já cadastrado."}

        if not nome:
            return {"status": "erro", "mensagem": "Nome é obrigatório."}

        if not senha:
            return {"status": "erro", "mensagem": "A senha deve ter pelo menos 6 caracteres."}

        novo = Usuario(
            nome_usuario=nome,
            email_usuario=email,
            senha_usuario=senha
        )

        db.session.add(novo)
        db.session.commit()

        return {"status": "ok", "mensagem": "Usuário cadastrado com sucesso."}

    # ----------------------------------------------------------
    # LOGIN
    # ----------------------------------------------------------
    def login(self, email, senha):
        usuario = Usuario.query.filter_by(email_usuario=email).first()

        if not usuario:
            return {"status": "erro", "mensagem": "E-mail não encontrado."}

        if usuario.senha_usuario != senha:
            return {"status": "erro", "mensagem": "Senha incorreta."}

        return {
            "status": "ok",
            "id": usuario.id_usuario,
            "nome": usuario.nome_usuario,
            "email": usuario.email_usuario,
        }

    # ----------------------------------------------------------
    # PROCURAR POR ID
    # ----------------------------------------------------------
    def procurar_por_id(self, user_id):
        return Usuario.query.get(user_id)

    # ----------------------------------------------------------
    # PROCURAR POR EMAIL
    # ----------------------------------------------------------
    def procurar_por_email(self, email):
        return Usuario.query.filter_by(email_usuario=email).first()

    # ----------------------------------------------------------
    # ATUALIZAR USUÁRIO
    # ----------------------------------------------------------
    def atualizar(self, user_id, nome, email, perfil, status):
        usuario = Usuario.query.get(user_id)

        if not usuario:
            return {"status": "erro", "mensagem": "Usuário não encontrado."}

        if not nome:
            return {"status": "erro", "mensagem": "Nome não pode ser vazio."}

        usuario.nome_usuario = nome
        usuario.email_usuario = email

        db.session.commit()

        return {"status": "ok", "mensagem": "Usuário atualizado."}

    # ----------------------------------------------------------
    # EXCLUIR (inativar)
    # ----------------------------------------------------------
    def excluir(self, user_id):
        usuario = Usuario.query.get(user_id)

        if not usuario:
            return {"status": "erro", "mensagem": "Usuário não encontrado."}

        usuario.status = "inativo"
        db.session.commit()

        return {"status": "ok", "mensagem": "Usuário inativado."}

    # ----------------------------------------------------------
    # LISTAR TODOS
    # ----------------------------------------------------------
    def listar_todos(self):
        return Usuario.query.all()
