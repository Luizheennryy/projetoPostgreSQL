import os
from dotenv import load_dotenv

import unittest
from db import PostgreSQL

class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        # Carrega .env.test sempre antes de cada teste
        load_dotenv(dotenv_path=".env.test", override=True)

    def test_connection(self):
        try:
            conn = PostgreSQL.get_connection()
            self.assertIsNotNone(conn)
            conn.close()
            print("✅ Conexão com banco passou!")
        except Exception as e:
            self.fail(f"Erro na conexão com o banco: {e}")
