# 🚀 Projeto PostgreSQL - Automação de Banco de Dados

Este projeto tem como objetivo **automatizar operações no PostgreSQL** usando Python.  
Inclui funcionalidades como **DELETE otimizado com backup**, **inserções automáticas**, **testes automatizados** e **integração contínua**.

---

## 📌 Funcionalidades

✅ **DELETE com Backup** antes da exclusão  
✅ **INSERT e UPDATE automáticos** para manter os dados atualizados  
✅ **Testes automatizados** com `unittest`  
✅ **Banco de testes isolado** para evitar alterações no banco principal  
✅ **Integração com GitHub Actions** para rodar testes automaticamente  

---

## 🚀 Como Rodar o Projeto

### **1️⃣ Criar o Ambiente Virtual**
```sh
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

pip install -r requirements.txt

pip install -r requirements.txt

TEST_MODE=True python -m scripts.setup_test_db

TEST_MODE=True python -m unittest discover -s tests

🛠 Tecnologias Utilizadas
Python 3.11
PostgreSQL
Unittest para testes
GitHub Actions para CI/CD

🔥 Integração com GitHub Actions
Os testes são executados automaticamente em cada git push.
Confira a aba "Actions" no repositório do GitHub para ver os resultados.

📜 Sobre o Autor
👤 Luiz Henrique dos Santos Vieira
🚀 Analista de Operações Comerciais III | Especialista em Automação de Banco de Dados

💼 Mais de 10 anos de experiência em análise de sistemas, desenvolvimento de relatórios, Dashboards e automação de processos
🎯 Atualmente trabalha na Claro Brasil, atuando na integração e tratamento de dados de diversos sistemas.
📊 Grande expertise em BI e desenvolvimento de Dashboards escaláveis

🛠 Habilidades:
✅ Python (Data Processing, Automação, Testes, SQL)
✅ Banco de Dados & SQL – Engenharia, ETL e Otimização
    Engenharia de Dados & ETL: Desenvolvimento e automação de pipelines ETL para extração, transformação e carga de dados em ambientes analíticos, garantindo performance e escalabilidade.
    Modelagem de Dados Relacional & Dimensional: Estruturação eficiente de bases de dados seguindo 3FN (terceira forma normal) e modelagem dimensional (Star Schema e Snowflake), otimizando consultas e armazenamento.
    Manipulação Avançada de Dados:
    Operações complexas (SELECT, INSERT, UPDATE, DELETE, MERGE, TRUNCATE).
    Joins eficientes (INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, CROSS JOIN).
    Filtragens (WHERE, HAVING, DISTINCT, GROUP BY, ORDER BY).
    Funções agregadas e de janela (SUM, AVG, ROW_NUMBER, RANK, PARTITION BY).
    Otimização de Consultas e Performance:
    Criação e manutenção de Índices Clusterizados e Não-Clusterizados para acelerar consultas.
    Uso eficiente de EXPLAIN ANALYZE para identificar gargalos e otimizar queries.
    Particionamento e paralelismo para manipulação de grandes volumes de dados.
    Gestão de Transações e Controle de Concorrência:
    Aplicação de ACID Transactions com BEGIN, COMMIT, ROLLBACK para garantir consistência dos dados.
    Gerenciamento de locks (ROW LOCK, TABLE LOCK) para evitar condições de corrida.
    Stored Procedures, Views e Triggers:
    Automação de regras de negócio no banco via Triggers e Stored Procedures.
    Criação de Views e Materialized Views para otimizar consultas frequentes.
    Administração e Segurança:
    Gestão de usuários e permissões (GRANT, REVOKE).
    Auditoria e logs para rastreamento de alterações e segurança dos dados.
    Backup e recuperação de dados para evitar perdas em cenários críticos.
    Experiência Multi-SGBD:
    PostgreSQL – Foco em Data Warehousing, particionamento e replicação.
    MySQL – Administração de sistemas OLTP, otimização de queries e replicação.
    Oracle – Desenvolvimento PL/SQL, Stored Procedures e manipulação de grandes volumes de dados.
✅ Power BI (DAX, M, Modelagem, Relatórios Dinâmicos)
✅ Microsoft Power Apps
✅ VBA e Automação de Processos
✅ Metodologias Ágeis


🔗 GitHub luizhennryy| 📧 Contato luizheennry@icloud.com

 Contribuição
Quer contribuir?

Faça um fork do repositório
Crie uma branch (git checkout -b minha-feature)
Commit suas alterações (git commit -m "Minha nova feature")
Dê um push na branch (git push origin minha-feature)
Abra um Pull Request


---

### **3️⃣ Adicionar ao GitHub**
Agora, adicione e envie o `README.md` para o repositório:

```sh
git add README.md
git commit -m "Adicionando README estruturado"
git push origin main
