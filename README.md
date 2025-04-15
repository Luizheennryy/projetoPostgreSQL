🚀 Projeto PostgreSQL - Automação de Banco de Dados

Este projeto tem como objetivo automatizar operações no PostgreSQL usando Python. Inclui funcionalidades como DELETE otimizado com auditoria, inserções automáticas, testes automatizados, e ambiente de testes isolado com unittest.

📌 Funcionalidades

✅ DELETE com auditoria (log das exclusões realizadas)✅ INSERT e UPDATE automáticos para manter os dados atualizados✅ Testes automatizados com unittest✅ Banco de testes isolado com .env.test e porta customizada✅ Logs informativos para rastreabilidade das operações✅ Integração com GitHub Actions para rodar testes automaticamente

🛠 Tecnologias Utilizadas

Python 3.11+

PostgreSQL (local na porta 5433 no modo de testes)

psycopg2, dotenv, unittest

GitHub Actions (CI/CD)

🚀 Como Rodar o Projeto

1️⃣ Clonar o repositório

git clone https://github.com/seuusuario/seurepo.git
cd seurepo

2️⃣ Criar o ambiente virtual e instalar dependências

python -m venv .venv
.venv\Scripts\activate  # Windows
# ou
source .venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

3️⃣ Criar os arquivos de ambiente

Crie os arquivos .env e .env.test:

.env: (produção)

HOST=localhost
PORT=5432
USER=postgres
PASSWD=22
DATABASE=projetos

.env.test: (para rodar testes)

HOST=localhost
PORT=5433
USER=postgres
PASSWD=22
DATABASE=projetos_test

🧪 A porta 5433 deve ser usada para o banco de testes local. Garanta que esteja rodando nessa porta!

4️⃣ Criar o banco de teste e tabelas mock

TEST_MODE=True python -m scripts.setup_test_db

5️⃣ Rodar os testes

TEST_MODE=True python -m unittest discover -s tests

🔥 GitHub Actions - Integração Contínua

Os testes automatizados são executados em cada git push.Você pode acompanhar os resultados na aba Actions do repositório.

👤 Sobre o Autor

Luiz Henrique dos Santos Vieira🎯 Database Analyst | Data Engineer | Automation Specialist | Python & SQL Expert | Business Intelligence 💼 Mais de 10 anos de experiência em análise de sistemas, dashboards e automação de processos📊 Atua na Claro Brasil, integrando dados de múltiplos sistemas com foco em inteligência analítica

🧠 Habilidades Técnicas

✅ Python (scripts, automações, testes, logs)✅ SQL Avançado (joins, funções de janela, otimização, views, triggers, auditoria)✅ Modelagem de Dados Relacional & Dimensional✅ ETL & Data Engineering (pipelines, particionamento, índices, transações ACID)✅ Power BI, DAX, M, Power Apps✅ VBA, Excel, Automação de Processos✅ Git, GitHub Actions, CI/CD, Metodologias Ágeis

🤝 Contribuição

Quer contribuir?

Faça um fork do repositório

Crie uma branch com sua feature: git checkout -b minha-feature

Commit suas alterações: git commit -m "feat: minha nova feature"

Envie a branch: git push origin minha-feature

Abra um Pull Request 🧠

📫 Contato

📧 Email: luizheennry@icloud.com🔗 GitHub: luizhennryy

