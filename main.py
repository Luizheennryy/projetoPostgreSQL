from delete.delete_data import deletar_periodo

if __name__ == '__main__':
    tabelas_periodo = ["fato_gross_up","Fato_UR", "analitico_assinaturas", "fato_portabilidade", "fato_mplay"]
    deletar_periodo(tabelas_periodo, "2025-03")
