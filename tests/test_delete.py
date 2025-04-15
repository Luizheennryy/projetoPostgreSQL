import unittest
from unittest.mock import patch
from delete.delete_data import deletar_periodo

class TestDeleteData(unittest.TestCase):

    @patch('delete.delete_data.registrar_auditoria')  # ← Aqui mockamos a auditoria
    @patch('delete.delete_data.execute_query')         # ← Aqui mockamos o execute_query
    def test_delete_muitas_linhas(self, mock_execute_query, mock_auditoria):
        """Testa DELETE quando há muitas linhas para deletar"""
        mock_execute_query.return_value = 1000  # Simula 1000 registros deletados

        deletar_periodo("Fato_UR", "2025-03")

        mock_execute_query.assert_called_once()
        mock_auditoria.assert_called_once_with("DELETE", "Fato_UR", 1000)
        print("✅ Teste de DELETE com muitas linhas passou!")

    @patch('delete.delete_data.registrar_auditoria')
    @patch('delete.delete_data.execute_query')
    def test_delete_sem_registros(self, mock_execute_query, mock_auditoria):
        """Testa DELETE quando não há registros no período"""
        mock_execute_query.return_value = 0  # Simula nenhum registro deletado

        deletar_periodo("Fato_UR", "2099-12")

        mock_execute_query.assert_called_once()
        mock_auditoria.assert_not_called()  # ← auditoria não deve ser chamada nesse caso
        print("✅ Teste de DELETE sem registros passou!")

if __name__ == '__main__':
    unittest.main()
