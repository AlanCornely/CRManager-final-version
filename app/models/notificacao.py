from app.database import db

class NotificacaoModel:
    """Modelo para a tabela NOTIFICACOES"""
    
    @staticmethod
    def create(data: dict):
        query = """
        INSERT INTO NOTIFICACOES (id_usuario, mensagem, tipo)
        VALUES (?, ?, ?)
        """
        params = (
            data.get('id_usuario'), # Pode ser None para notificações globais
            data['mensagem'],
            data.get('tipo', 'info')
        )
        return db.execute_query(query, params)
    
    @staticmethod
    def get_recent(limit: int = 50, id_usuario: int = None):
        """Busca notificações recentes (globais ou do usuário)"""
        query = """
        SELECT * FROM NOTIFICACOES 
        WHERE (id_usuario IS NULL OR id_usuario = ?) 
        ORDER BY data_criacao DESC LIMIT ?
        """
        params = (id_usuario, limit)
        return db.execute_query(query, params)
        
    @staticmethod
    def get_unread_count(id_usuario: int = None):
        query = """
        SELECT COUNT(*) as count FROM NOTIFICACOES 
        WHERE (id_usuario IS NULL OR id_usuario = ?) AND lida = 0
        """
        result = db.execute_query(query, (id_usuario,), fetch_one=True)
        return result['count'] if result else 0

    @staticmethod
    def mark_as_read(id_notificacao: int):
        query = "UPDATE NOTIFICACOES SET lida = 1 WHERE id_notificacao = ?"
        return db.execute_query(query, (id_notificacao,))
    
    @staticmethod
    def mark_all_as_read(id_usuario: int = None):
        query = "UPDATE NOTIFICACOES SET lida = 1 WHERE (id_usuario IS NULL OR id_usuario = ?) AND lida = 0"
        return db.execute_query(query, (id_usuario,))
