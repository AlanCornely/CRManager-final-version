-- 1. Tabela CATEGORIAS
CREATE TABLE CATEGORIAS (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT
);

-- 2. Tabela FORNECEDORES
CREATE TABLE FORNECEDORES (
    id_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    empresa VARCHAR(255) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    cnpj VARCHAR(18) UNIQUE NOT NULL,
    inscricao_estadual VARCHAR(20),
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco VARCHAR(255),
    cidade VARCHAR(100),
    estado VARCHAR(50),
    pais VARCHAR(50),
    cep VARCHAR(10),
    contato_responsavel VARCHAR(100),
    prazo_entrega_dias INT,
    condicoes_pagamento TEXT
);

-- 3. Tabela USUARIOS
CREATE TABLE USUARIOS (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    cargo VARCHAR(50),
    permissao VARCHAR(50),
    ativo BOOLEAN DEFAULT TRUE
);

-- 4. Tabela CLIENTES
CREATE TABLE CLIENTES (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    cpf_cnpj VARCHAR(18) UNIQUE,
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco VARCHAR(255),
    cidade VARCHAR(100),
    estado VARCHAR(50)
);

-- 5. Tabela PRODUTOS
CREATE TABLE PRODUTOS (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    categoria_id INT,
    sku VARCHAR(50) UNIQUE,
    codigo_barras VARCHAR(50) UNIQUE,
    estoque_minimo INT DEFAULT 0,
    estoque_maximo INT,
    quantidade_atual INT DEFAULT 0,
    unidade_medida VARCHAR(20),
    preco_custo DECIMAL(10, 2) NOT NULL,
    preco_venda DECIMAL(10, 2) NOT NULL,
    localizacao VARCHAR(100),
    fornecedor_id_padrao INT,
    data_cadastro DATE NOT NULL,
    ativo BOOLEAN DEFAULT TRUE,
    
    FOREIGN KEY (categoria_id) REFERENCES CATEGORIAS(id_categoria),
    FOREIGN KEY (fornecedor_id_padrao) REFERENCES FORNECEDORES(id_fornecedor)
);

-- 6. Tabela VENDAS
CREATE TABLE VENDAS (
    id_venda INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    usuario_id INT NOT NULL,
    data_venda DATETIME NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    forma_pagamento VARCHAR(50),
    
    FOREIGN KEY (cliente_id) REFERENCES CLIENTES(id_cliente),
    FOREIGN KEY (usuario_id) REFERENCES USUARIOS(id_usuario)
);

-- 7. Tabela ITENS_VENDA
CREATE TABLE ITENS_VENDA (
    id_item_venda INT PRIMARY KEY AUTO_INCREMENT,
    id_venda INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    valor_unitario DECIMAL(10, 2) NOT NULL,
    
    FOREIGN KEY (id_venda) REFERENCES VENDAS(id_venda),
    FOREIGN KEY (id_produto) REFERENCES PRODUTOS(id_produto)
);

-- 8. Tabela COMPRAS
CREATE TABLE COMPRAS (
    id_compra INT PRIMARY KEY AUTO_INCREMENT,
    fornecedor_id INT NOT NULL,
    usuario_id INT NOT NULL,
    data_compra DATETIME NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    numero_nf VARCHAR(50) UNIQUE,
    
    FOREIGN KEY (fornecedor_id) REFERENCES FORNECEDORES(id_fornecedor),
    FOREIGN KEY (usuario_id) REFERENCES USUARIOS(id_usuario)
);

-- 9. Tabela ITENS_COMPRA
CREATE TABLE ITENS_COMPRA (
    id_item_compra INT PRIMARY KEY AUTO_INCREMENT,
    compra_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,
    valor_unitario DECIMAL(10, 2) NOT NULL,
    
    FOREIGN KEY (compra_id) REFERENCES COMPRAS(id_compra),
    FOREIGN KEY (produto_id) REFERENCES PRODUTOS(id_produto)
);

-- 10. Tabela MOVIMENTACOES
CREATE TABLE MOVIMENTACOES (
    id_movimentacao INT PRIMARY KEY AUTO_INCREMENT,
    produto_id INT NOT NULL,
    tipo VARCHAR(20) NOT NULL, -- Ex: 'ENTRADA', 'SAIDA', 'AJUSTE'
    quantidade INT NOT NULL,
    motivo TEXT,
    usuario_id INT NOT NULL,
    data_movimentacao DATETIME NOT NULL,
    valor_unitario DECIMAL(10, 2),
    nota_fiscal VARCHAR(50),
    
    FOREIGN KEY (produto_id) REFERENCES PRODUTOS(id_produto),
    FOREIGN KEY (usuario_id) REFERENCES USUARIOS(id_usuario)
);

-- 11. Tabela ALERTAS
CREATE TABLE ALERTAS (
    id_alerta INT PRIMARY KEY AUTO_INCREMENT,
    produto_id INT NOT NULL,
    tipo VARCHAR(50) NOT NULL, -- Ex: 'ESTOQUE_BAIXO', 'VENCIMENTO'
    descricao TEXT,
    status VARCHAR(20) DEFAULT 'PENDENTE', -- Ex: 'PENDENTE', 'RESOLVIDO'
    data_criacao DATETIME NOT NULL,
    
    FOREIGN KEY (produto_id) REFERENCES PRODUTOS(id_produto)
);
