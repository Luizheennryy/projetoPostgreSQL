🚀 PostgreSQL Project – Database Automation
This project aims to automate PostgreSQL operations using Python. It includes features such as optimized DELETE with audit logging, automated inserts, unit testing, and an isolated test environment using unittest.

📌 Features
✅ DELETE with audit logging (tracking of deleted records)
✅ Automatic INSERT and UPDATE to keep data up to date
✅ Automated testing using unittest
✅ Isolated test database using .env.test and custom port
✅ Informative logs for traceability
✅ GitHub Actions integration to run tests automatically

🛠 Technologies Used
Python 3.11+

PostgreSQL (local instance on port 5433 for test mode)

psycopg2, dotenv, unittest

GitHub Actions (CI/CD)

🚀 How to Run the Project
1️⃣ Clone the repository
bash
Copiar
Editar
git clone https://github.com/youruser/yourrepo.git
cd yourrepo
2️⃣ Create a virtual environment and install dependencies
bash
Copiar
Editar
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
3️⃣ Create environment files
Create the .env and .env.test files:

.env (production):

ini
Copiar
Editar
HOST=localhost  
PORT=5432  
USER=postgres  
PASSWD=22  
DATABASE=projetos
.env.test (for test runs):

ini
Copiar
Editar
HOST=localhost  
PORT=5433  
USER=postgres  
PASSWD=22  
DATABASE=projetos_test
🧪 Ensure PostgreSQL is running locally on port 5433 for test mode!

4️⃣ Setup test database and mock tables
bash
Copiar
Editar
TEST_MODE=True python -m scripts.setup_test_db
5️⃣ Run tests
bash
Copiar
Editar
TEST_MODE=True python -m unittest discover -s tests
🔥 GitHub Actions – Continuous Integration
All tests are executed automatically on every git push.
You can track results in the Actions tab of the GitHub repository.

👤 About the Author
Luiz Henrique dos Santos Vieira
🎯 Database Analyst | Data Engineer | Automation Specialist | Python & SQL Expert | Business Intelligence

💼 10+ years of experience in systems analysis, dashboards, and process automation
📊 Currently at Claro Brasil, integrating data from multiple systems with a focus on analytics and smart insights

🧠 Technical Skills
✅ Python (scripting, automation, testing, logging)
✅ Advanced SQL (joins, window functions, optimization, views, triggers, auditing)
✅ Relational & Dimensional Data Modeling
✅ ETL & Data Engineering (pipelines, partitioning, indexing, ACID transactions)
✅ Power BI, DAX, M Language, Power Apps
✅ VBA, Excel, Process Automation
✅ Git, GitHub Actions, CI/CD, Agile Methodologies

🤝 Contributions Welcome
Want to contribute?

Fork the repository

Create a feature branch: git checkout -b my-feature

Commit your changes: git commit -m "feat: my new feature"

Push the branch: git push origin my-feature

Open a Pull Request 🧠
