import unittest
from db import PostgreSQL

class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        try:
            conn = PostgreSQL.get_connection()
            self.assertIsNotNone(conn)
            conn.close()
        except Exception as e:
            self.fail(f"Erro na conexão com o banco: {e}")

if __name__ == '__main__':
    unittest.main()
