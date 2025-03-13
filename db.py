import os
import psycopg2
from dotenv import load_dotenv
from utils.logger import setup_logger

# 🔍 Forçar a leitura correta do .env
if os.getenv("TEST_MODE") == "True":
    print("🔍 MODO TESTE ATIVADO: Carregando .env.test")
    load_dotenv(dotenv_path=".env.test", override=True)  # 🔹 Agora forçamos o override!
else:
    load_dotenv(dotenv_path=".env", override=True)

# Configuração do Logger
logger = setup_logger("db_logger", "logs/db.log")

class PostgreSQL:
    @staticmethod
    def get_connection():
        """Cria uma conexão com o banco correto"""
        try:
            database_name = os.getenv("DATABASE")  # Pegar o nome correto
            conn = psycopg2.connect(
                host=os.getenv("HOST"),
                port=os.getenv("PORT"),
                user=os.getenv("USER"),
                password=os.getenv("PASSWD"),
                database=database_name
            )
            print(f"✅ Conectado ao banco: {database_name}")  # 🔹 Confirmação no terminal
            return conn
        except psycopg2.Error as e:
            logger.error(f"Erro ao conectar ao PostgreSQL: {e}")
            raise
