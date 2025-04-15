import os
from dotenv import load_dotenv

import unittest
from db import PostgreSQL

class TestInsertQuery(unittest.TestCase):

    def setUp(self):
        # Força carregamento do .env.test ANTES da conexão
        load_dotenv(dotenv_path=".env.test", override=True)

        self.conn = PostgreSQL.get_connection()
        with self.conn.cursor() as cur:
            cur.execute('INSERT INTO "Fato_UR" (ano_mes, dados) VALUES (%s, %s);', ('2025-03', 'Teste de inserção'))
        self.conn.commit()

    def tearDown(self):
        with self.conn.cursor() as cur:
            cur.execute('DELETE FROM "Fato_UR" WHERE ano_mes = %s;', ('2025-03',))
        self.conn.commit()
        self.conn.close()

    def test_insercao(self):
        with self.conn.cursor() as cur:
            cur.execute('SELECT COUNT(*) FROM "Fato_UR" WHERE ano_mes = %s;', ('2025-03',))
            result = cur.fetchone()
        self.assertEqual(result[0], 1)
        print("✅ Teste de inserção passou!")

    def test_consulta(self):
        with self.conn.cursor() as cur:
            cur.execute('SELECT dados FROM "Fato_UR" WHERE ano_mes = %s;', ('2025-03',))
            result = cur.fetchone()
        self.assertEqual(result[0], 'Teste de inserção')
        print("✅ Teste de consulta passou!")
