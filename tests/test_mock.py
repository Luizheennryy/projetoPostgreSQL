import unittest
from unittest.mock import patch
from delete.delete_data import deletar_periodo

class TestDeleteData(unittest.TestCase):

    @patch('delete.delete_data.registrar_auditoria')
    @patch('delete.delete_data.execute_query')
    def test_delete(self, mock_execute_query, mock_auditoria):
        """Testa se o DELETE está sendo chamado corretamente"""
        mock_execute_query.return_value = 5

        deletar_periodo("Fato_UR", "2025-03")

        mock_execute_query.assert_called_once()
        mock_auditoria.assert_called_once_with("DELETE", "Fato_UR", 5)
        print("✅ Teste de chamada de DELETE com auditoria passou!")

if __name__ == '__main__':
    unittest.main()
