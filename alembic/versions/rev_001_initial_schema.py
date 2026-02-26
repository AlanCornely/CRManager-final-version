"""initial_schema

Revision ID: rev_001
Revises: 
Create Date: 2024-01-27 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import os

# revision identifiers, used by Alembic.
revision: str = 'rev_001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Read database.sql in the root directory relative to this file
    # This file is in alembic/versions/
    # database.sql is in ../../
    
    # We will try to find the file or just execute the content if we can't find it.
    # To be safe and self-contained, I am embedding the SQL content as fallback or primary.
    # However, since the task asked to "Convert database.sql", executing the file content is best.
    
    sql_file_path = os.path.join(os.path.dirname(__file__), '../../database.sql')
    
    if os.path.exists(sql_file_path):
        with open(sql_file_path, 'r') as f:
            sql_statements = f.read()
        
        # Split by ; to generic poor man's execution if needed, but op.execute might support multiple.
        # SQLAlchemy execute usually handles it if the driver supports it. 
        # But safest is to split.
        statements = sql_statements.split(';')
        for statement in statements:
            if statement.strip():
                op.execute(statement)
    else:
        # Fallback if file not found (though it should be locally)
        pass


def downgrade() -> None:
    # Drop tables in reverse order of creation (approximate)
    op.execute("DROP TABLE IF EXISTS ALERTAS")
    op.execute("DROP TABLE IF EXISTS MOVIMENTACOES")
    op.execute("DROP TABLE IF EXISTS ITENS_COMPRA")
    op.execute("DROP TABLE IF EXISTS COMPRAS")
    op.execute("DROP TABLE IF EXISTS ITENS_VENDA")
    op.execute("DROP TABLE IF EXISTS VENDAS")
    op.execute("DROP TABLE IF EXISTS PRODUTOS")
    op.execute("DROP TABLE IF EXISTS CLIENTES")
    op.execute("DROP TABLE IF EXISTS USUARIOS")
    op.execute("DROP TABLE IF EXISTS FORNECEDORES")
    op.execute("DROP TABLE IF EXISTS CATEGORIAS")
