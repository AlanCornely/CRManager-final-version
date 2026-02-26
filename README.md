# CRM COM GESTÃO DE ESTOQUE - CRManager

**Autor:** Alan M. Cornely

**Data:** 25 de Novembro de 2025

**Versão:** 2.0 (Com Detalhamento de Telas)

---

## 1. Introdução e Visão Geral

Este documento define o escopo do projeto para o desenvolvimento de um **Sistema de CRM (Customer Relationship Management) com Foco em Gestão de Estoque**. O objetivo principal é integrar as funcionalidades de relacionamento com o cliente com a gestão eficiente do inventário, permitindo uma visão unificada e estratégica das operações de vendas e logística.

O sistema visa otimizar processos, reduzir erros de estoque, melhorar a precisão das previsões de vendas e, consequentemente, aumentar a satisfação do cliente e a rentabilidade da empresa.

### Problemas que o sistema resolve:
*   Falta de controle de entradas/saídas de estoque.
*   Integração ruim entre vendas e estoque.
*   Dificuldade em rastrear produtos, pedidos e clientes.

### Público-alvo:
Empresas que vendem produtos físicos (lojas, distribuidoras, e-commerce, etc.).

---

## 2. Objetivos e Critérios de Sucesso

| Categoria | Objetivo | Descrição | Critério de Sucesso |
| :--- | :--- | :--- | :--- |
| **Gestão de Estoque** | Otimização do Inventário | Reduzir o excesso de estoque e a falta de produtos (ruptura), garantindo níveis ideais. | Redução de **90%** nas divergências de estoque identificadas durante os inventários físicos. |
| **Relacionamento com o Cliente** | Visão 360º do Cliente | Centralizar todas as interações e histórico de pedidos do cliente para um atendimento personalizado. | O CRM deve armazenar **histórico de contato** e **histórico de compras** para todos os clientes. |
| **Processos** | Automação de Fluxos | Automatizar a atualização de estoque após vendas e a geração de alertas de reabastecimento. | Redução de **20%** no tempo gasto pela equipe de vendas para processar um pedido. |
| **Tomada de Decisão** | Relatórios e Análises | Fornecer dados em tempo real sobre o desempenho de vendas, giro de estoque e lucratividade por produto/cliente. | Todos os relatórios devem exportar para **PDF/Excel**. |

---

## 3. Funcionalidades Chave (Módulos Principais)



### 3.1. Módulo de Clientes (CRM)
*   **Cadastro Completo:** Clientes (empresa/pessoa), armazenamento de dados de contato e preferências.
*   **Histórico:** Histórico de compras e histórico de atendimento.
*   **Comunicação:** Registro de contato (ligações, WhatsApp, e-mails) e notas de reuniões.
*   **Funil de Vendas:** Rastreamento do pipeline (Prospecção → Contato → Proposta → Negociação → Fechamento).
*   **Gestão de Oportunidades:** Rastreamento do pipeline de vendas, desde o lead até a conversão.
*   **Agendamento e Lembretes** (follow-up).
*   **Análise de Clientes:** Ticket médio, produtos mais comprados, perfil de compra.

### 3.2. Módulo de Produtos
*   **Cadastro Detalhado:** SKU/código interno, nome, descrição, unidade de medida, fornecedor, preço de custo e venda, categoria.
*   **Variações:** Cadastro de variações (tamanho, cor, modelo).
*   **Mídia:** Fotos e documentos anexos.

### 3.3. Módulo de Estoque (Inventário)
*   **Movimentação:** Registro de Entradas (compra, devolução, ajuste) e Saídas (venda, consumo interno, perda).
*   **Detalhes da Movimentação:** Movimentações detalhadas com data, usuário e motivo.
*   **Localização:** Controle de múltiplos depósitos/locais (armazéns, corredores, prateleiras).
*   **Controle de Nível:** Mínimo e máximo por produto.
*   **Alertas:** Alerta de reposição automática (estoque mínimo).
*   **Inventário Físico:** Ferramenta para contagem e ajuste de estoque, com registro de Divergências (esperado vs. encontrado).

### 3.4. Módulo de Pedidos / Vendas
*   **Criação:** Criação de orçamentos e conversão para pedido.
*   **Disponibilidade:** Consulta em tempo real da disponibilidade de estoque.
*   **Reserva de Estoque:** Capacidade de reservar itens para pedidos em andamento ou cotações.
*   **Baixa Automática:** Baixa automática após venda.
*   **Faturamento:** Emissão de nota fiscal (se aplicável) e integração com faturamento.
*   **Status do Pedido:** Em análise, Aprovado, Separação, Enviado, Concluído.

### 3.5. Módulo de Fornecedores
*   **Cadastro:** Cadastro de fornecedores.
*   **Histórico:** Histórico de compras.
*   **Performance:** Análise de performance (prazo, preço, qualidade).
*   **Pedidos de Compra:** Cotação, Aprovação, Recebimento e Baixa automática no estoque.

### 3.6. Módulo Financeiro (Opcional/Básico)
*   Contas a pagar (ligado à compra).
*   Contas a receber (ligado às vendas).
*   Relatórios financeiros básicos.
*   Conciliação básica.
*   *Nota: Funcionalidades avançadas de contabilidade e folha de pagamento estão **fora do escopo**.*

### 3.7. Dashboard e Relatórios
*   **Dashboard:** Nível de estoque, Ações pendentes, Funil de vendas, Acompanhar histórico do cliente.
*   **Relatórios Principais:** Ruptura de estoque, Curva ABC de produtos, Produtos mais vendidos, Estoque parado, Vendas por cliente, Projeção de compras, Comparativo de preços, Giro de Estoque, Previsão de Demanda (básica).

---

## 4. Detalhamento das Telas (Web Application)

O sistema será acessado via interface web, com as seguintes telas principais:

### 4.1. Telas de Autenticação
*   **Tela de Login:** Formulário simples com campos de e-mail e senha. Opções para recuperar senha ou criar nova conta.
*   **Tela de Cadastro/Registro:** Formulário para criação de novas contas de usuário (interno).
*   **Tela de Recuperação de Senha:** Fluxo para redefinição de senha via e-mail.

### 4.2. Dashboard (Tela Inicial)
*   **Visão Geral:** Exibe um resumo das métricas mais importantes.
*   **Widgets Principais:**
    *   Nível de Estoque (Gráfico de status geral).
    *   Funil de Vendas (Status das oportunidades).
    *   Ações Pendentes (Alertas de estoque mínimo, pedidos em análise).
    *   Vendas Recentes (Lista de últimos pedidos).
    *   Ticket Médio e Produtos Mais Vendidos (Gráficos de análise rápida).

### 4.3. Módulo de Clientes (CRM)

*   **Lista de Clientes:** Tabela ou lista paginada com filtros (nome, status, ticket médio). Botões de ação (abrir, editar, excluir).
*   **Detalhes do Cliente (Visão 360º):** Tela principal com abas para:
    *   **Informações Básicas:** Dados de contato, endereço.
    *   **Histórico de Compras:** Lista de todos os pedidos e orçamentos.
    *   **Histórico de Atendimento/Comunicação:** Linha do tempo de interações (ligações, e-mails, WhatsApp, notas de reuniões).
    *   **Oportunidades/Funil:** Rastreamento das negociações ativas.
    *   **Análise:** Ticket médio, produtos preferidos.
*   **Criar/Editar Cliente:** Formulário para cadastro completo.

### 4.4. Módulo de Produtos

*   **Lista de Produtos:** Tabela com filtros (SKU, nome, categoria, fornecedor). Exibe estoque atual, preço de custo e venda. Botões de ação (abrir, editar, excluir).
*   **Criar/Editar Produto:** Formulário detalhado com campos para:
    *   SKU, Nome, Descrição.
    *   Preços (Custo, Venda).
    *   Categoria, Fornecedor.
    *   Gestão de Variações (tamanho, cor, modelo).
    *   Upload de Fotos e Documentos.
    *   Definição de Estoque Mínimo/Máximo.

### 4.5. Módulo de Estoque (Inventário)

*   **Movimentações de Estoque:** Tabela com histórico de todas as entradas e saídas. Filtros por data, tipo de movimento, produto e usuário.
*   **Entrada de Estoque:** Formulário para registrar compras, devoluções ou ajustes positivos. Campos: Produto, Quantidade, Local, Fornecedor, Data, Motivo.
*   **Saída de Estoque:** Formulário para registrar vendas (automático via Pedidos), consumo interno ou perdas. Campos: Produto, Quantidade, Local, Motivo.
*   **Inventário Físico:** Tela para iniciar e gerenciar contagens.
    *   Lista de contagens em andamento/concluídas.
    *   Ferramenta de contagem (leitura de código de barras ou inserção manual).
    *   Relatório de Divergências (esperado vs. encontrado) com opção de ajuste.
*   **Alertas de Reposição:** Lista de produtos abaixo do estoque mínimo, com opção de gerar Pedido de Compra.

### 4.6. Módulo de Pedidos / Vendas

*   **Lista de Pedidos/Orçamentos:** Tabela com filtros (status, cliente, data, vendedor). Exibe status atual.
*   **Criar/Editar Pedido:** Formulário para:
    *   Seleção do Cliente.
    *   Adição de Produtos (com consulta de disponibilidade em tempo real).
    *   Cálculo de valores.
    *   Reserva de Estoque.
    *   Definição de Status (Em análise, Aprovado, etc.).
    *   Opção de conversão de Orçamento para Pedido.

### 4.7. Módulo de Fornecedores

*   **Lista de Fornecedores:** Tabela com dados básicos e histórico de compras.
*   **Detalhes do Fornecedor:** Informações de contato, lista de produtos fornecidos e análise de performance (prazo, preço).
*   **Pedidos de Compra:** Lista de pedidos de compra feitos ao fornecedor, com status (Cotação, Aprovação, Recebimento).

### 4.8. Módulo de Relatórios

*   **Seleção de Relatório:** Menu com opções de relatórios (Curva ABC, Giro de Estoque, Ruptura, Vendas por Cliente, etc.).
*   **Visualização e Filtros:** Tela de exibição do relatório com filtros de período, categoria, etc.
*   **Exportação:** Botão para exportar para PDF/Excel.

### 4.9. Configurações e Usuários

*   **Gestão de Usuários:** Lista de usuários do sistema com seus perfis de acesso (Administrador, Vendedor, Estoquista).
*   **Gestão de Permissões:** Tela para definir e ajustar os níveis de acesso.
*   **Configurações Gerais:** Opções para configurar integrações, regras de negócio (ex: não permitir estoque negativo) e dados da empresa.

---

## 5. Fluxos de Trabalho (Workflows) e Regras de Negócio



### 5.1. Fluxos de Trabalho
*   **Fluxo de Venda:** Cliente cria pedido → Estoque reserva item → Pedido aprovado → Estoque dá baixa → Entrega → Registro no CRM.
*   **Fluxo de Compra:** Solicitação → Cotação → Pedido → Recebimento → Entrada no estoque.

### 5.2. Regras de Negócio
*   Produtos **não podem** ficar com estoque negativo.
*   Venda só acontece se houver **quantidade mínima** disponível.
*   Cada usuário só pode editar o que estiver dentro do seu **nível de permissão**.
*   Histórico **não pode ser apagado** (apenas inativado).
*   Cada movimentação deve registrar **usuário, data e motivo**.

---

## 6. Requisitos Técnicos e Não Funcionais



| Tipo | Requisito | Detalhe |
| :--- | :--- | :--- |
| **Tecnologia** | Stack de Desenvolvimento | Python (ou Node.js), Vue e MySQL. |
| **Backend** | Arquitetura | python (talvez node) |
| **Frontend** | Arquitetura | vue |
| **App Mobile** | Mobile | flutter |
| **Banco de Dados** | Armazenamento | MySQL |
| **Autenticação** | Acesso | JWT, OAuth, Autenticação de dois fatores (2FA) opcional. |
| **Segurança** | Proteção de Dados | Criptografia SSL/TLS, Criptografia de dados sensíveis, Conformidade com LGPD, Backup automático. |
| **API** | Integração Externa | API REST pública para comunicação com outros sistemas. |
| **Controle** | Logs | Logs de alteração e Permissões/Níveis de acesso. |
| **Performance** | Tempo de Resposta | O tempo de carregamento de páginas e relatórios críticos não deve exceder **3 segundos**. |
| **Disponibilidade** | Uptime | O sistema deve ter uma disponibilidade mínima de **99,5%**. |
| **Usabilidade** | Interface | A interface deve ser limpa, intuitiva e responsiva (desktop e mobile via navegador). |

---

## 7. Escopo Fora do Projeto (Out-of-Scope)



É importante definir o que o projeto **não** irá contemplar para evitar desvios de escopo:
*   **Integração com Sistemas Externos:** Não inclui integração nativa com ERPs, sistemas de contabilidade ou plataformas de e-commerce de terceiros (a API REST pública será o ponto de integração).
*   **Módulo Financeiro Completo:** Não inclui funcionalidades avançadas de contas a pagar/receber, conciliação bancária ou folha de pagamento.
*   **Logística e Rastreamento de Entregas:** Não inclui gestão de frota, roteirização ou rastreamento em tempo real de transportadoras.
*   **Análise Preditiva Avançada:** A previsão de demanda será básica (baseada em médias históricas), sem uso de modelos complexos de Machine Learning.
*   **PDV** (ponto de venda).
*   **Gestão fiscal avançada.**
*   **Funcionalidades industriais** (BOM, produção, etc.).

---

## 8. Cronograma e Próximos Passos

*(Adicionado o detalhamento de fases do N4, adaptado para o tema CRM/Estoque)*

### 8.1. Fases do Projeto:
1.  Levantamento e prototipação (incluindo a aprovação formal deste escopo).
2.  Arquitetura do sistema e especificações técnicas detalhadas (*wireframes*).
3.  Desenvolvimento por módulos.
4.  Testes.
5.  Treinamento para usuários-chave e documentação de uso.
6.  Implantação.
7.  Suporte pós-lançamento.

### 8.2. Detalhamento das Fases

| Fase | Duração Estimada | Foco Principal | Entregáveis Chave |
| :--- | :--- | :--- | :--- |
| **1. Setup de Infraestrutura** | 1 Semana | Configuração do ambiente e banco de dados. | Repositório pronto, Schema DB, Documentação base. |
| **2. Fundação Back-end** | 2 Semanas | Implementação do sistema de Autenticação e API base. | Sistema de Login/Registro funcional, API de Autenticação testada. |
| **3. API de Gestão (Clientes/Produtos)** | 2 Semanas | Criação dos endpoints CRUD para Clientes e Produtos. | API completa de Clientes e Produtos (incluindo variações). |
| **4. API de Estoque e Vendas** | 2 Semanas | Criação dos endpoints para Movimentação de Estoque e Pedidos. | API de Estoque (Entrada/Saída/Inventário) e API de Pedidos/Vendas. |
| **5. Web App - Parte 1 (Base e CRM)** | 2 Semanas | Criação da interface de Autenticação, Dashboard e Módulo de Clientes. | Web App com Login, Dashboard e Gestão de Clientes (CRUD). |
| **6. Web App - Parte 2 (Estoque e Vendas)** | 2 Semanas | Implementação dos Módulos de Produtos, Estoque, Pedidos e Fornecedores. | Web App completo com todos os módulos de gestão. |
| **7. Relatórios e Funcionalidades Extras** | 1 Semana | Implementação do Módulo de Relatórios e Configurações. | Módulo de Relatórios (Exportação PDF/Excel) e Gestão de Usuários/Permissões. |
| **8. Testes e Refinamento** | 1 Semana | Testes abrangentes, correção de bugs e otimização. | Aplicação totalmente testada, performance otimizada, documentação finalizada. |

### 8.3. Próximos Passos Imediatos:
1.  **Aprovação do Escopo:** Revisão e aprovação formal deste documento pelas partes interessadas.
2.  **Levantamento Detalhado:** Criação de *wireframes* e especificações técnicas detalhadas para cada tela descrita na Seção 4.
3.  **Planejamento:** Definição do cronograma, alocação de recursos e estimativa de custos.
4.  **Desenvolvimento:** Início da fase de codificação e testes.

## 9. Guia de Manutenção e Desenvolvimento

### 9.1. Gestão de Banco de Dados (Alembic)
O projeto utiliza Alembic para versionamento do esquema do banco de dados.

*   **Aplicar migrações (Atualizar banco):**
    ```bash
    alembic upgrade head
    ```

*   **Criar nova migração:**
    ```bash
    alembic revision -m "mensagem_da_mudanca"
    ```

### 9.2. Backup do Banco de Dados
Um script de backup automatizado está disponível na raiz do projeto (`backup.sh`).

*   **Executar backup:**
    ```bash
    ./backup.sh
    ```
    O arquivo gerado será salvo na pasta `backups/` com timestamp.
