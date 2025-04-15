from db import PostgreSQL
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def criar_tabelas_teste():
    with PostgreSQL.get_connection() as conn:
        with conn.cursor() as cur:
            # Tabela de auditoria
            cur.execute("""
                CREATE TABLE IF NOT EXISTS log_auditoria (
                    id SERIAL PRIMARY KEY,
                    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    usuario TEXT DEFAULT current_user,
                    operacao TEXT,
                    tabela_afetada TEXT,
                    registros_afetados INT
                );
            """)

            # Tabela fato_gross_up
            cur.execute("""
                CREATE TABLE IF NOT EXISTS fato_gross_up (
                    id SERIAL PRIMARY KEY,
                    ano_mes TEXT NOT NULL,
                    valor NUMERIC
                );
            """)

            # Tabela Fato_UR usada nos testes
            cur.execute("""
                CREATE TABLE IF NOT EXISTS "Fato_UR" (
                    id SERIAL PRIMARY KEY,
                    ano_mes VARCHAR(7),
                    dados TEXT
                );

            """)

            # Inserindo dados mock para testes
            cur.execute("""
                INSERT INTO "Fato_UR" (ano_mes, dados) VALUES
                    ('2025-03', 'Mock 1'),
                    ('2025-03', 'Mock 2'),
                    ('2025-03', 'Mock 3');

            """)

            conn.commit()
            print("✅ Todas as tabelas criadas e dados mock inseridos com sucesso!")

if __name__ == "__main__":
    print("🔍 Configurando o banco de testes...")
    criar_tabelas_teste()
    print("✅ Banco de testes configurado!")
