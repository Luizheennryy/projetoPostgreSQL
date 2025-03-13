import unittest
from db import PostgreSQL

class TestInsertQuery(unittest.TestCase):

    def setUp(self):
        """Configura o banco de testes antes de cada teste"""
        self.conn = PostgreSQL.get_connection()
        with self.conn.cursor() as cur:
            cur.execute('INSERT INTO "Fato_UR" (ano_mes, dados) VALUES (%s, %s);', ('2025-03', 'Teste de inserção'))
        self.conn.commit()

    def tearDown(self):
        """Limpa os dados após cada teste"""
        with self.conn.cursor() as cur:
            cur.execute('DELETE FROM "Fato_UR" WHERE ano_mes = %s;', ('2025-03',))
        self.conn.commit()
        self.conn.close()

    def test_insercao(self):
        """Testa se a inserção foi bem-sucedida"""
        with self.conn.cursor() as cur:
            cur.execute('SELECT COUNT(*) FROM "Fato_UR" WHERE ano_mes = %s;', ('2025-03',))
            result = cur.fetchone()
        self.assertEqual(result[0], 1)
        print("✅ Teste de inserção passou!")

    def test_consulta(self):
        """Testa se a consulta retorna os dados corretos"""
        with self.conn.cursor() as cur:
            cur.execute('SELECT dados FROM "Fato_UR" WHERE ano_mes = %s;', ('2025-03',))
            result = cur.fetchone()
        self.assertEqual(result[0], 'Teste de inserção')
        print("✅ Teste de consulta passou!")

if __name__ == '__main__':
    unittest.main()
