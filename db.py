import os
from dotenv import load_dotenv
import psycopg2

class PostgreSQL:
    @staticmethod
    def get_connection():
        # Carrega o .env.test se TEST_MODE estiver ativo
        if os.getenv("TEST_MODE") == "True":
            load_dotenv(dotenv_path=".env.test", override=True)
            print(f"🔎 DB_HOST: {os.getenv('DB_HOST')}")
            print(f"🔎 DB_PORT: {os.getenv('DB_PORT')}")
            print(f"🔎 DB_USER: {os.getenv('DB_USER')}")
            print(f"🔎 DB_PASSWORD: {os.getenv('DB_PASSWORD')}")
            print(f"🔎 DB_NAME: {os.getenv('DB_NAME')}")
        else:
            load_dotenv(dotenv_path=".env", override=True)
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn
