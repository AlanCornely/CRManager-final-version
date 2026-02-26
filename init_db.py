#!/usr/bin/env python3
"""
Database initialization script for SQLite CRM system
Converts MySQL schema to SQLite and creates the database
"""

import sqlite3
import os

DB_PATH = "crm_estoque.db"

# SQLite-compatible schema
SCHEMA = """
-- 1. Tabela CATEGORIAS
CREATE TABLE IF NOT EXISTS CATEGORIAS (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT
);

-- 2. Tabela FORNECEDORES
CREATE TABLE IF NOT EXISTS FORNECEDORES (
    id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa TEXT NOT NULL,
    razao_social TEXT NOT NULL,
    cnpj TEXT UNIQUE NOT NULL,
    inscricao_estadual TEXT,
    email TEXT,
    telefone TEXT,
    endereco TEXT,
    cidade TEXT,
    estado TEXT,
    pais TEXT,
    cep TEXT,
    contato_responsavel TEXT,
    prazo_entrega_dias INTEGER,
    condicoes_pagamento TEXT
);

-- 3. Tabela USUARIOS
CREATE TABLE IF NOT EXISTS USUARIOS (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    cargo TEXT,
    permissao TEXT,
    ativo INTEGER DEFAULT 1
);

-- 4. Tabela CLIENTES
CREATE TABLE IF NOT EXISTS CLIENTES (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf_cnpj TEXT UNIQUE,
    email TEXT,
    telefone TEXT,
    endereco TEXT,
    cidade TEXT,
    estado TEXT
);

-- 5. Tabela PRODUTOS
CREATE TABLE IF NOT EXISTS PRODUTOS (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    categoria_id INTEGER,
    sku TEXT UNIQUE,
    codigo_barras TEXT UNIQUE,
    estoque_minimo INTEGER DEFAULT 0,
    estoque_maximo INTEGER,
    quantidade_atual INTEGER DEFAULT 0,
    unidade_medida TEXT,
    preco_custo REAL NOT NULL,
    preco_venda REAL NOT NULL,
    localizacao TEXT,
    fornecedor_id_padrao INTEGER,
    data_cadastro TEXT NOT NULL,
    ativo INTEGER DEFAULT 1,
    
    FOREIGN KEY (categoria_id) REFERENCES CATEGORIAS(id_categoria),
    FOREIGN KEY (fornecedor_id_padrao) REFERENCES FORNECEDORES(id_fornecedor)
);

-- 6. Tabela VENDAS
CREATE TABLE IF NOT EXISTS VENDAS (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    usuario_id INTEGER NOT NULL,
    data_venda TEXT NOT NULL,
    valor_total REAL NOT NULL,
    forma_pagamento TEXT,
    
    FOREIGN KEY (cliente_id) REFERENCES CLIENTES(id_cliente),
    FOREIGN KEY (usuario_id) REFERENCES USUARIOS(id_usuario)
);

-- 7. Tabela ITENS_VENDA
CREATE TABLE IF NOT EXISTS ITENS_VENDA (
    id_item_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    id_venda INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_unitario REAL NOT NULL,
    
    FOREIGN KEY (id_venda) REFERENCES VENDAS(id_venda),
    FOREIGN KEY (id_produto) REFERENCES PRODUTOS(id_produto)
);

-- 8. Tabela COMPRAS
CREATE TABLE IF NOT EXISTS COMPRAS (
    id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
    fornecedor_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,
    data_compra TEXT NOT NULL,
    valor_total REAL NOT NULL,
    numero_nf TEXT UNIQUE,
    
    FOREIGN KEY (fornecedor_id) REFERENCES FORNECEDORES(id_fornecedor),
    FOREIGN KEY (usuario_id) REFERENCES USUARIOS(id_usuario)
);

-- 9. Tabela ITENS_COMPRA
CREATE TABLE IF NOT EXISTS ITENS_COMPRA (
    id_item_compra INTEGER PRIMARY KEY AUTOINCREMENT,
    compra_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_unitario REAL NOT NULL,
    
    FOREIGN KEY (compra_id) REFERENCES COMPRAS(id_compra),
    FOREIGN KEY (produto_id) REFERENCES PRODUTOS(id_produto)
);

-- 10. Tabela MOVIMENTACOES
CREATE TABLE IF NOT EXISTS MOVIMENTACOES (
    id_movimentacao INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    motivo TEXT,
    usuario_id INTEGER NOT NULL,
    data_movimentacao TEXT NOT NULL,
    valor_unitario REAL,
    nota_fiscal TEXT,
    
    FOREIGN KEY (produto_id) REFERENCES PRODUTOS(id_produto),
    FOREIGN KEY (usuario_id) REFERENCES USUARIOS(id_usuario)
);

-- 11. Tabela ALERTAS
CREATE TABLE IF NOT EXISTS ALERTAS (
    id_alerta INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    descricao TEXT,
    status TEXT DEFAULT 'PENDENTE',
    data_criacao TEXT NOT NULL,
    
    FOREIGN KEY (produto_id) REFERENCES PRODUTOS(id_produto)
);
"""

def init_database():
    """Initialize SQLite database with schema"""
    # Remove existing database if exists
    if os.path.exists(DB_PATH):
        print(f"⚠️  Database {DB_PATH} already exists. Removing...")
        os.remove(DB_PATH)
    
    print(f"📦 Creating database: {DB_PATH}")
    
    try:
        # Create connection
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Enable foreign keys
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        # Execute schema
        cursor.executescript(SCHEMA)
        conn.commit()
        
        print("✅ Database created successfully!")
        print("✅ All tables created:")
        
        # List all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            print(f"   - {table[0]}")
        
        conn.close()
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Error creating database: {e}")
        return False

if __name__ == "__main__":
    init_database()
