class UsuarioRN:

    def __init__(self, conexao):
        self.conn = conexao

    # ----------------------------------------------------------
    # CADASTRAR USUÁRIO
    # ----------------------------------------------------------
    def cadastrar(self, usuario):
        sql_verifica = """
            SELECT id FROM usuarios WHERE email = %s
        """
        with self.conn.cursor() as cur:
            cur.execute(sql_verifica, (usuario.email,))
            existe = cur.fetchone()

            if existe:
                return "E-mail já cadastrado."

        if not usuario.nome:
            return "Nome é obrigatório."

        if not usuario.senha or len(usuario.senha) < 6:
            return "A senha deve ter pelo menos 6 caracteres."

        sql_insert = """
            INSERT INTO usuarios (nome, email, senha, perfil, status)
            VALUES (%s, %s, %s, %s, %s)
        """
        with self.conn.cursor() as cur:
            cur.execute(sql_insert, (
                usuario.nome,
                usuario.email,
                usuario.senha,
                usuario.perfil,
                usuario.status
            ))
            self.conn.commit()

        return "Usuário cadastrado com sucesso."

    # ----------------------------------------------------------
    # LOGIN
    # ----------------------------------------------------------
    def login(self, email, senha):
        sql = """
            SELECT id, nome, email, senha, perfil, status
            FROM usuarios
            WHERE email = %s
        """
        with self.conn.cursor() as cur:
            cur.execute(sql, (email,))
            usuario = cur.fetchone()

        if not usuario:
            return "E-mail não encontrado."

        if usuario[5] != "ativo":
            return "Usuário inativo."

        if senha != usuario[3]:
            return "Senha incorreta."

        return {
            "id": usuario[0],
            "nome": usuario[1],
            "email": usuario[2],
            "perfil": usuario[4],
            "status": usuario[5]
        }

    # ----------------------------------------------------------
    # PROCURAR POR ID
    # ----------------------------------------------------------
    def procurar_por_id(self, user_id):
        sql = """
            SELECT id, nome, email, perfil, status
            FROM usuarios
            WHERE id = %s
        """
        with self.conn.cursor() as cur:
            cur.execute(sql, (user_id,))
            return cur.fetchone()

    # ----------------------------------------------------------
    # PROCURAR POR E-MAIL
    # ----------------------------------------------------------
    def procurar_por_email(self, email):
        sql = """
            SELECT id, nome, email, perfil, status
            FROM usuarios
            WHERE email = %s
        """
        with self.conn.cursor() as cur:
            cur.execute(sql, (email,))
            return cur.fetchone()

    # ----------------------------------------------------------
    # ATUALIZAR USUÁRIO
    # ----------------------------------------------------------
    def atualizar(self, usuario):
        if not usuario.nome:
            return "Nome não pode ser vazio."

        sql = """
            UPDATE usuarios
            SET nome = %s, email = %s, perfil = %s, status = %s
            WHERE id = %s
        """
        with self.conn.cursor() as cur:
            cur.execute(sql, (
                usuario.nome,
                usuario.email,
                usuario.perfil,
                usuario.status,
                usuario.id
            ))
            self.conn.commit()

        return "Usuário atualizado."

    # ----------------------------------------------------------
    # EXCLUIR (inativar)
    # ----------------------------------------------------------
    def excluir(self, user_id):
        sql = """
            UPDATE usuarios
            SET status = 'inativo'
            WHERE id = %s
        """
        with self.conn.cursor() as cur:
            cur.execute(sql, (user_id,))
            self.conn.commit()

        return "Usuário inativado."

    # ----------------------------------------------------------
    # LISTAR TODOS
    # ----------------------------------------------------------
    def listar_todos(self):
        sql = """
            SELECT id, nome, email, perfil, status
            FROM usuarios
        """
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
