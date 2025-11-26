class Usuario:
    def __init__(self, id, nome, email, senha, criado_em=None, atualizado_em=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.criado_em = criado_em
        self.atualizado_em = atualizado_em

    def __repr__(self):
        return f"<Usuario {self.id} - {self.email}>"
