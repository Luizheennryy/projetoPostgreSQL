import unittest
import timeit
from db import PostgreSQL

class TestPerformance(unittest.TestCase):
    def test_tempo_delete(self):
        """Mede o tempo de execução do DELETE"""
        setup_code = "from delete.delete_data import deletar_periodo"
        test_code = "deletar_periodo('Fato_UR', '2025-03')"
        tempo_execucao = timeit.timeit(test_code, setup=setup_code, number=3)
        print(f"Tempo médio para deletar: {tempo_execucao:.4f} segundos")

if __name__ == '__main__':
    unittest.main()
