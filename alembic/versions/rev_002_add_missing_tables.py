"""add_missing_tables

Revision ID: rev_002
Revises: rev_001
Create Date: 2024-01-27 12:05:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'rev_002'
down_revision: Union[str, None] = 'rev_001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. depositos
    op.create_table(
        'depositos',
        sa.Column('id_deposito', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('nome', sa.String(100), nullable=False),
        sa.Column('endereco', sa.String(255), nullable=True),
        sa.Column('ativo', sa.Boolean(), server_default='1', nullable=False)
    )

    # 2. historico_comunicacao
    op.create_table(
        'historico_comunicacao',
        sa.Column('id_comunicacao', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('cliente_id', sa.Integer(), nullable=False),
        sa.Column('tipo', sa.String(50), nullable=False), # LIGACAO, WHATSAPP, etc.
        sa.Column('data_contato', sa.DateTime(), nullable=False),
        sa.Column('notas', sa.Text(), nullable=True),
        sa.Column('usuario_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['cliente_id'], ['CLIENTES.id_cliente'], ),
        sa.ForeignKeyConstraint(['usuario_id'], ['USUARIOS.id_usuario'], )
    )

    # 3. oportunidades
    op.create_table(
        'oportunidades',
        sa.Column('id_oportunidade', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('cliente_id', sa.Integer(), nullable=False),
        sa.Column('titulo', sa.String(150), nullable=False),
        sa.Column('valor_estimado', sa.Numeric(15, 2), nullable=True),
        sa.Column('status', sa.String(50), nullable=False), # PROSPECCAO, etc.
        sa.Column('data_criacao', sa.DateTime(), nullable=False),
        sa.Column('data_fechamento_estimada', sa.Date(), nullable=True),
        sa.Column('usuario_responsavel_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['cliente_id'], ['CLIENTES.id_cliente'], ),
        sa.ForeignKeyConstraint(['usuario_responsavel_id'], ['USUARIOS.id_usuario'], )
    )

    # 4. produto_variacoes
    op.create_table(
        'produto_variacoes',
        sa.Column('id_variacao', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('produto_id', sa.Integer(), nullable=False),
        sa.Column('nome_variacao', sa.String(100), nullable=False),
        sa.Column('sku_variacao', sa.String(50), nullable=True),
        sa.Column('quantidade', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('preco_adicional', sa.Numeric(10, 2), nullable=True, server_default='0.00'),
        sa.ForeignKeyConstraint(['produto_id'], ['PRODUTOS.id_produto'], )
    )

    # 5. logs_atividade
    op.create_table(
        'logs_atividade',
        sa.Column('id_log', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('usuario_id', sa.Integer(), nullable=False),
        sa.Column('acao', sa.String(100), nullable=False),
        sa.Column('tabela_afetada', sa.String(50), nullable=True),
        sa.Column('registro_id', sa.Integer(), nullable=True),
        sa.Column('detalhes', sa.Text(), nullable=True),
        sa.Column('data_hora', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['usuario_id'], ['USUARIOS.id_usuario'], )
    )

    # 6. avaliacoes_fornecedor
    op.create_table(
        'avaliacoes_fornecedor',
        sa.Column('id_avaliacao', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('fornecedor_id', sa.Integer(), nullable=False),
        sa.Column('nota_prazo', sa.Integer(), nullable=True),
        sa.Column('nota_qualidade', sa.Integer(), nullable=True),
        sa.Column('nota_preco', sa.Integer(), nullable=True),
        sa.Column('comentario', sa.Text(), nullable=True),
        sa.Column('data_avaliacao', sa.DateTime(), nullable=False),
        sa.Column('usuario_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['fornecedor_id'], ['FORNECEDORES.id_fornecedor'], ),
        sa.ForeignKeyConstraint(['usuario_id'], ['USUARIOS.id_usuario'], )
    )


def downgrade() -> None:
    op.drop_table('avaliacoes_fornecedor')
    op.drop_table('logs_atividade')
    op.drop_table('produto_variacoes')
    op.drop_table('oportunidades')
    op.drop_table('historico_comunicacao')
    op.drop_table('depositos')
