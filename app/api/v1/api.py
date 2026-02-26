from fastapi import APIRouter
from . import usuarios, produtos, notificacoes  # categorias, fornecedores, clientes, vendas, compras, movimentos

api_router = APIRouter()

api_router.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
api_router.include_router(produtos.router, prefix="/produtos", tags=["Produtos"])
api_router.include_router(notificacoes.router, prefix="/notificacoes", tags=["Notificações"])
# TODO: Implement the following routers
# api_router.include_router(categorias.router, prefix="/categorias", tags=["Categorias"])
# api_router.include_router(fornecedores.router, prefix="/fornecedores", tags=["Fornecedores"])
# api_router.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
# api_router.include_router(vendas.router, prefix="/vendas", tags=["Vendas"])
# api_router.include_router(compras.router, prefix="/compras", tags=["Compras"])
# api_router.include_router(movimentos.router, prefix="/movimentos", tags=["Movimentações"])