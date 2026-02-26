from app.database import db

class CategoriaModel:
    """Modelo para a tabela CATEGORIAS"""
    
    @staticmethod
    def create(nome: str, descricao: str = None):
        query = """
        INSERT INTO CATEGORIAS (nome, descricao)
        VALUES (%s, %s)
        """
        return db.execute_query(query, (nome, descricao))
    
    @staticmethod
    def get_all():
        query = "SELECT * FROM CATEGORIAS ORDER BY nome"
        return db.execute_query(query)
    
    @staticmethod
    def get_by_id(id_categoria: int):
        query = "SELECT * FROM CATEGORIAS WHERE id_categoria = %s"
        return db.execute_query(query, (id_categoria,), fetch_one=True)
    
    @staticmethod
    def update(id_categoria: int, nome: str = None, descricao: str = None):
        query = """
        UPDATE CATEGORIAS 
        SET nome = COALESCE(%s, nome),
            descricao = COALESCE(%s, descricao)
        WHERE id_categoria = %s
        """
        return db.execute_query(query, (nome, descricao, id_categoria))
    
    @staticmethod
    def delete(id_categoria: int):
        query = "DELETE FROM CATEGORIAS WHERE id_categoria = %s"
        return db.execute_query(query, (id_categoria,))