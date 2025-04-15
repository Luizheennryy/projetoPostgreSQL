import psycopg2
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo correto
if os.getenv("TEST_MODE"):
    load_dotenv(".env.test")
else:
    load_dotenv(".env")

class PostgreSQLConnection:
    @staticmethod
    def get_connection():
        """Cria e retorna uma conexão com o banco de dados"""
        return psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 5432))  # Forçar a conversão para inteiro
        )
