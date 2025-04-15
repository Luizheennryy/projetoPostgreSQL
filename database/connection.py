import os
import psycopg2
from dotenv import load_dotenv

# Carrega variáveis do ambiente de teste ou produção
if os.getenv("TEST_MODE") == "True":
    load_dotenv(".env.test")
else:
    load_dotenv(".env")

class PostgreSQLConnection:
    @staticmethod
    def get_connection():
        return psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT"))  # SEM DEFAULT!
        )
