from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from app.schemas.produto import ProdutoCreate, ProdutoUpdate, ProdutoInDB
from app.models.produto import ProdutoModel
from app.models.categoria import CategoriaModel
from app.models.fornecedor import FornecedorModel

router = APIRouter()

@router.post("/", response_model=dict)
async def criar_produto(produto: ProdutoCreate):
    """Cria um novo produto"""
    # Verifica se categoria existe
    if produto.categoria_id:
        categoria = CategoriaModel.get_by_id(produto.categoria_id)
        if not categoria:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Categoria não encontrada"
            )
    
    # Verifica se fornecedor existe
    if produto.fornecedor_id_padrao:
        fornecedor = FornecedorModel.get_by_id(produto.fornecedor_id_padrao)
        if not fornecedor:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Fornecedor não encontrado"
            )
    
    # Verifica se SKU já existe
    if produto.sku:
        existing_sku = ProdutoModel.get_by_sku(produto.sku)
        if existing_sku:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="SKU já cadastrado"
            )
    
    produto_id = ProdutoModel.create(produto.dict())
    return {"id_produto": produto_id, "message": "Produto criado com sucesso"}

@router.get("/", response_model=List[ProdutoInDB])
async def listar_produtos(
    categoria_id: Optional[int] = Query(None),
    ativo: Optional[bool] = Query(True)
):
    """Lista todos os produtos"""
    produtos = ProdutoModel.get_all()
    
    # Filtros
    filtered_produtos = []
    for produto in produtos:
        if categoria_id and produto['categoria_id'] != categoria_id:
            continue
        if ativo is not None and produto['ativo'] != ativo:
            continue
        filtered_produtos.append(produto)
    
    return filtered_produtos

@router.get("/baixo-estoque", response_model=List[ProdutoInDB])
async def listar_baixo_estoque():
    """Lista produtos com estoque abaixo do mínimo"""
    produtos = ProdutoModel.get_baixo_estoque()
    return produtos

@router.get("/{id_produto}", response_model=ProdutoInDB)
async def buscar_produto(id_produto: int):
    """Busca um produto por ID"""
    produto = ProdutoModel.get_by_id(id_produto)
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    return produto

@router.put("/{id_produto}")
async def atualizar_produto(id_produto: int, produto: ProdutoUpdate):
    """Atualiza um produto"""
    # Verifica se produto existe
    existing = ProdutoModel.get_by_id(id_produto)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    
    # Verifica se categoria existe
    if produto.categoria_id:
        categoria = CategoriaModel.get_by_id(produto.categoria_id)
        if not categoria:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Categoria não encontrada"
            )
    
    result = ProdutoModel.update(id_produto, produto.dict(exclude_unset=True))
    if result:
        return {"message": "Produto atualizado com sucesso"}
    
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Erro ao atualizar produto"
    )

@router.patch("/{id_produto}/estoque")
async def ajustar_estoque(
    id_produto: int,
    quantidade: int = Query(..., description="Quantidade positiva para adicionar, negativa para remover")
):
    """Ajusta estoque do produto"""
    result = ProdutoModel.update_estoque(id_produto, quantidade)
    if result:
        return {"message": "Estoque ajustado com sucesso"}
    
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Erro ao ajustar estoque"
    )

@router.delete("/{id_produto}")
async def deletar_produto(id_produto: int):
    """Remove um produto"""
    result = ProdutoModel.delete(id_produto)
    if result:
        return {"message": "Produto deletado com sucesso"}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Produto não encontrado"
    )