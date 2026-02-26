from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    categoria_id: Optional[int] = None
    sku: Optional[str] = None
    codigo_barras: Optional[str] = None
    estoque_minimo: Optional[int] = 0
    estoque_maximo: Optional[int] = None
    quantidade_atual: Optional[int] = 0
    unidade_medida: Optional[str] = None
    preco_custo: float
    preco_venda: float
    localizacao: Optional[str] = None
    fornecedor_id_padrao: Optional[int] = None
    ativo: Optional[bool] = True

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    categoria_id: Optional[int] = None
    sku: Optional[str] = None
    codigo_barras: Optional[str] = None
    estoque_minimo: Optional[int] = None
    estoque_maximo: Optional[int] = None
    quantidade_atual: Optional[int] = None
    unidade_medida: Optional[str] = None
    preco_custo: Optional[float] = None
    preco_venda: Optional[float] = None
    localizacao: Optional[str] = None
    fornecedor_id_padrao: Optional[int] = None
    ativo: Optional[bool] = None

class ProdutoInDB(ProdutoBase):
    id_produto: int
    data_cadastro: date
    categoria_nome: Optional[str] = None
    fornecedor_nome: Optional[str] = None

    class Config:
        from_attributes = True