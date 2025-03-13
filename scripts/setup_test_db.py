import sys
import os
import psycopg2
from db import PostgreSQL

# Garante que o script pode importar corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def criar_tabelas_teste():
    """Cria a estrutura de tabelas no banco de testes antes dos testes rodarem."""
    conn = PostgreSQL.get_connection()

    queries = [
        """
        CREATE TABLE IF NOT EXISTS "Fato_UR" (
            id SERIAL PRIMARY KEY,
            ano_mes VARCHAR(7),
            dados TEXT
        );
        """
    ]

    with conn.cursor() as cur:
        for query in queries:
            cur.execute(query)
        conn.commit()

    print("✅ Banco de testes configurado com sucesso! Tabela Fato_UR criada.")
    conn.close()

if __name__ == "__main__":
    criar_tabelas_teste()
