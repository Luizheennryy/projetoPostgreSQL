import unittest
from unittest.mock import patch, MagicMock
from delete.delete_data import deletar_periodo

class TestDeleteData(unittest.TestCase):

    @patch('db.PostgreSQL.get_connection')
    def test_delete(self, mock_get_connection):
        """Testa se o DELETE está sendo chamado corretamente"""
        
        # Criando um mock da conexão e do cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_get_connection.return_value = mock_conn

        # Executando a função de delete
        deletar_periodo("Fato_UR", "2025-03")

        # Testando se o cursor.execute foi chamado
        self.assertTrue(mock_cursor.execute.called, "O método execute() não foi chamado!")

if __name__ == '__main__':
    unittest.main()
