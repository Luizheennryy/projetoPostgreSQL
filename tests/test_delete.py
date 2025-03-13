import unittest
from unittest.mock import patch, MagicMock
from delete.delete_data import deletar_periodo
from db import PostgreSQL

class TestDeleteData(unittest.TestCase):

    @patch('db.PostgreSQL.get_connection')
    def test_delete_muitas_linhas(self, mock_get_connection):
        """Testa DELETE quando há muitas linhas para deletar"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1000  # Simula 1000 registros deletados
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_get_connection.return_value = mock_conn

        deletar_periodo("Fato_UR", "2025-03")

        mock_cursor.execute.assert_called()
        print("✅ Teste de DELETE com muitas linhas passou!")

    @patch('db.PostgreSQL.get_connection')
    def test_delete_sem_registros(self, mock_get_connection):
        """Testa DELETE quando não há registros no período"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 0  # Simula que nenhuma linha foi afetada
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_get_connection.return_value = mock_conn

        deletar_periodo("Fato_UR", "2099-12")  # Período sem registros

        mock_cursor.execute.assert_called()
        print("✅ Teste de DELETE sem registros passou!")

if __name__ == '__main__':
    unittest.main()
