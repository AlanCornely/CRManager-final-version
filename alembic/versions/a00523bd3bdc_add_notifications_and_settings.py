"""add_notifications_and_settings

Revision ID: a00523bd3bdc
Revises: rev_002
Create Date: 2026-02-03 19:05:15.936747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a00523bd3bdc'
down_revision: Union[str, None] = 'rev_002'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add configuracoes column to USUARIOS
    op.execute("ALTER TABLE USUARIOS ADD COLUMN configuracoes TEXT DEFAULT '{}'")
    
    # Create NOTIFICACOES table
    op.execute("""
    CREATE TABLE NOTIFICACOES (
        id_notificacao INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        mensagem TEXT NOT NULL,
        tipo TEXT DEFAULT 'info',
        lida BOOLEAN DEFAULT 0,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_usuario) REFERENCES USUARIOS (id_usuario)
    )
    """)


def downgrade() -> None:
    op.execute("DROP TABLE NOTIFICACOES")
    # SQLite does not support DROP COLUMN easily in older versions, 
    # but for this we might skip or use a more complex recreation. 
    # For now, we will leave the column or use advanced alembic if needed.
    # Since we use raw sql, we just keep it simple.
    pass
