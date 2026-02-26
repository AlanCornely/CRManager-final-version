from app.database import db
from datetime import date

class ProdutoModel:
    """Modelo para a tabela PRODUTOS"""
    
    @staticmethod
    def create(data: dict):
        query = """
        INSERT INTO PRODUTOS (
            nome, descricao, categoria_id, sku, codigo_barras,
            estoque_minimo, estoque_maximo, quantidade_atual,
            unidade_medida, preco_custo, preco_venda, localizacao,
            fornecedor_id_padrao, data_cadastro, ativo
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            data['nome'], data.get('descricao'), data.get('categoria_id'),
            data.get('sku'), data.get('codigo_barras'),
            data.get('estoque_minimo', 0), data.get('estoque_maximo'),
            data.get('quantidade_atual', 0), data.get('unidade_medida'),
            data['preco_custo'], data['preco_venda'], data.get('localizacao'),
            data.get('fornecedor_id_padrao'), date.today(),
            data.get('ativo', True)
        )
        return db.execute_query(query, params)
    
    @staticmethod
    def get_all():
        query = """
        SELECT p.*, c.nome as categoria_nome, f.empresa as fornecedor_nome
        FROM PRODUTOS p
        LEFT JOIN CATEGORIAS c ON p.categoria_id = c.id_categoria
        LEFT JOIN FORNECEDORES f ON p.fornecedor_id_padrao = f.id_fornecedor
        ORDER BY p.nome
        """
        return db.execute_query(query)
    
    @staticmethod
    def get_by_id(id_produto: int):
        query = """
        SELECT p.*, c.nome as categoria_nome, f.empresa as fornecedor_nome
        FROM PRODUTOS p
        LEFT JOIN CATEGORIAS c ON p.categoria_id = c.id_categoria
        LEFT JOIN FORNECEDORES f ON p.fornecedor_id_padrao = f.id_fornecedor
        WHERE p.id_produto = %s
        """
        return db.execute_query(query, (id_produto,), fetch_one=True)
    
    @staticmethod
    def get_by_sku(sku: str):
        query = "SELECT * FROM PRODUTOS WHERE sku = %s"
        return db.execute_query(query, (sku,), fetch_one=True)
    
    @staticmethod
    def update(id_produto: int, data: dict):
        query = """
        UPDATE PRODUTOS SET
            nome = COALESCE(%s, nome),
            descricao = COALESCE(%s, descricao),
            categoria_id = COALESCE(%s, categoria_id),
            sku = COALESCE(%s, sku),
            codigo_barras = COALESCE(%s, codigo_barras),
            estoque_minimo = COALESCE(%s, estoque_minimo),
            estoque_maximo = COALESCE(%s, estoque_maximo),
            quantidade_atual = COALESCE(%s, quantidade_atual),
            unidade_medida = COALESCE(%s, unidade_medida),
            preco_custo = COALESCE(%s, preco_custo),
            preco_venda = COALESCE(%s, preco_venda),
            localizacao = COALESCE(%s, localizacao),
            fornecedor_id_padrao = COALESCE(%s, fornecedor_id_padrao),
            ativo = COALESCE(%s, ativo)
        WHERE id_produto = %s
        """
        params = (
            data.get('nome'), data.get('descricao'), data.get('categoria_id'),
            data.get('sku'), data.get('codigo_barras'),
            data.get('estoque_minimo'), data.get('estoque_maximo'),
            data.get('quantidade_atual'), data.get('unidade_medida'),
            data.get('preco_custo'), data.get('preco_venda'),
            data.get('localizacao'), data.get('fornecedor_id_padrao'),
            data.get('ativo'), id_produto
        )
        return db.execute_query(query, params)
    
    @staticmethod
    def update_estoque(id_produto: int, quantidade: int):
        """Atualiza quantidade em estoque"""
        query = """
        UPDATE PRODUTOS 
        SET quantidade_atual = quantidade_atual + %s
        WHERE id_produto = %s
        """
        return db.execute_query(query, (quantidade, id_produto))
    
    @staticmethod
    def get_baixo_estoque():
        """Retorna produtos com estoque abaixo do mínimo"""
        query = """
        SELECT p.*, c.nome as categoria_nome
        FROM PRODUTOS p
        LEFT JOIN CATEGORIAS c ON p.categoria_id = c.id_categoria
        WHERE p.quantidade_atual <= p.estoque_minimo AND p.ativo = TRUE
        """
        return db.execute_query(query)
    
    @staticmethod
    def delete(id_produto: int):
        query = "DELETE FROM PRODUTOS WHERE id_produto = %s"
        return db.execute_query(query, (id_produto,))