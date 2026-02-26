from app.database import db

class FornecedorModel:
    """Modelo para a tabela FORNECEDORES"""
    
    @staticmethod
    def create(data: dict):
        query = """
        INSERT INTO FORNECEDORES (
            empresa, razao_social, cnpj, inscricao_estadual, email,
            telefone, endereco, cidade, estado, pais, cep,
            contato_responsavel, prazo_entrega_dias, condicoes_pagamento
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            data['empresa'], data['razao_social'], data['cnpj'],
            data.get('inscricao_estadual'), data.get('email'),
            data.get('telefone'), data.get('endereco'), data.get('cidade'),
            data.get('estado'), data.get('pais'), data.get('cep'),
            data.get('contato_responsavel'), data.get('prazo_entrega_dias'),
            data.get('condicoes_pagamento')
        )
        return db.execute_query(query, params)
    
    @staticmethod
    def get_all():
        query = "SELECT * FROM FORNECEDORES ORDER BY empresa"
        return db.execute_query(query)
    
    @staticmethod
    def get_by_id(id_fornecedor: int):
        query = "SELECT * FROM FORNECEDORES WHERE id_fornecedor = %s"
        return db.execute_query(query, (id_fornecedor,), fetch_one=True)
    
    @staticmethod
    def get_by_cnpj(cnpj: str):
        query = "SELECT * FROM FORNECEDORES WHERE cnpj = %s"
        return db.execute_query(query, (cnpj,), fetch_one=True)
    
    @staticmethod
    def update(id_fornecedor: int, data: dict):
        query = """
        UPDATE FORNECEDORES SET
            empresa = COALESCE(%s, empresa),
            razao_social = COALESCE(%s, razao_social),
            cnpj = COALESCE(%s, cnpj),
            inscricao_estadual = COALESCE(%s, inscricao_estadual),
            email = COALESCE(%s, email),
            telefone = COALESCE(%s, telefone),
            endereco = COALESCE(%s, endereco),
            cidade = COALESCE(%s, cidade),
            estado = COALESCE(%s, estado),
            pais = COALESCE(%s, pais),
            cep = COALESCE(%s, cep),
            contato_responsavel = COALESCE(%s, contato_responsavel),
            prazo_entrega_dias = COALESCE(%s, prazo_entrega_dias),
            condicoes_pagamento = COALESCE(%s, condicoes_pagamento)
        WHERE id_fornecedor = %s
        """
        params = (
            data.get('empresa'), data.get('razao_social'), data.get('cnpj'),
            data.get('inscricao_estadual'), data.get('email'),
            data.get('telefone'), data.get('endereco'), data.get('cidade'),
            data.get('estado'), data.get('pais'), data.get('cep'),
            data.get('contato_responsavel'), data.get('prazo_entrega_dias'),
            data.get('condicoes_pagamento'), id_fornecedor
        )
        return db.execute_query(query, params)
    
    @staticmethod
    def delete(id_fornecedor: int):
        query = "DELETE FROM FORNECEDORES WHERE id_fornecedor = %s"
        return db.execute_query(query, (id_fornecedor,))