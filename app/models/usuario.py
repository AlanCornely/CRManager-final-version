from app.database import db
import bcrypt

class UsuarioModel:
    """Modelo para a tabela USUARIOS"""
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        """Verifica se a senha está correta"""
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    @staticmethod
    def get_password_hash(password: str):
        """Gera hash da senha"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def create(data: dict):
        # Default settings
        import json
        config = json.dumps(data.get('configuracoes', {}))
        
        query = """
        INSERT INTO USUARIOS (nome, email, senha_hash, cargo, permissao, ativo, configuracoes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        hashed_password = UsuarioModel.get_password_hash(data['senha'])
        params = (
            data['nome'], data['email'], hashed_password,
            data.get('cargo'), data.get('permissao'), data.get('ativo', True),
            config
        )
        return db.execute_query(query, params)
    
    @staticmethod
    def get_all():
        query = "SELECT id_usuario, nome, email, cargo, permissao, ativo, configuracoes FROM USUARIOS"
        results = db.execute_query(query)
        # Parse JSON config if needed, or leave as string
        # For API consistency, it's often better to return dicts, but let's see how the API handles it.
        # We will parse it here.
        import json
        if results:
            for user in results:
                if user.get('configuracoes'):
                    try:
                        user['configuracoes'] = json.loads(user['configuracoes'])
                    except:
                        user['configuracoes'] = {}
        return results
    
    @staticmethod
    def get_by_id(id_usuario: int):
        query = "SELECT id_usuario, nome, email, cargo, permissao, ativo, configuracoes FROM USUARIOS WHERE id_usuario = ?"
        user = db.execute_query(query, (id_usuario,), fetch_one=True)
        if user and user.get('configuracoes'):
            import json
            try:
                user['configuracoes'] = json.loads(user['configuracoes'])
            except:
                user['configuracoes'] = {}
        return user
    
    @staticmethod
    def get_by_email(email: str):
        query = "SELECT * FROM USUARIOS WHERE email = ?"
        user = db.execute_query(query, (email,), fetch_one=True)
        if user and user.get('configuracoes'):
            import json
            try:
                user['configuracoes'] = json.loads(user['configuracoes'])
            except:
                user['configuracoes'] = {}
        return user
    
    @staticmethod
    def authenticate(email: str, password: str):
        """Autentica usuário"""
        user = UsuarioModel.get_by_email(email)
        if not user:
            return None
        
        if not UsuarioModel.verify_password(password, user['senha_hash']):
            return None
        
        # Remove senha do resultado
        user.pop('senha_hash', None)
        return user
    
    @staticmethod
    def update(id_usuario: int, data: dict):
        import json
        
        # Prepare params handling optional fields
        fields = []
        params = []
        
        if 'nome' in data:
            fields.append("nome = ?")
            params.append(data['nome'])
        if 'email' in data:
            fields.append("email = ?")
            params.append(data['email'])
        if 'cargo' in data:
            fields.append("cargo = ?")
            params.append(data['cargo'])
        if 'permissao' in data:
            fields.append("permissao = ?")
            params.append(data['permissao'])
        if 'ativo' in data:
            fields.append("ativo = ?")
            params.append(data['ativo'])
        if 'configuracoes' in data:
            fields.append("configuracoes = ?")
            params.append(json.dumps(data['configuracoes']))
            
        if not fields:
            return None
            
        query = f"UPDATE USUARIOS SET {', '.join(fields)} WHERE id_usuario = ?"
        params.append(id_usuario)
        
        return db.execute_query(query, tuple(params))
    
    @staticmethod
    def update_password(id_usuario: int, new_password: str):
        """Atualiza senha do usuário"""
        hashed_password = UsuarioModel.get_password_hash(new_password)
        query = "UPDATE USUARIOS SET senha_hash = ? WHERE id_usuario = ?"
        return db.execute_query(query, (hashed_password, id_usuario))
    
    @staticmethod
    def delete(id_usuario: int):
        query = "DELETE FROM USUARIOS WHERE id_usuario = ?"
        return db.execute_query(query, (id_usuario,))