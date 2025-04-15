from db import PostgreSQL
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Script para configurar o banco de testes
def setup_database():
    try:
        with PostgreSQL.get_connection() as conn:
            with conn.cursor() as cur:
                # Criar tabela de auditoria se não existir
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
                conn.commit()
                logger.info("✅ Banco de testes configurado com sucesso! Tabela log_auditoria criada.")
    except Exception as e:
        logger.error(f"❌ Erro ao configurar o banco de testes: {e}")

if __name__ == "__main__":
    setup_database()

def criar_tabelas_teste():
    with PostgreSQL.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS fato_gross_up (
                    id SERIAL PRIMARY KEY,
                    ano_mes TEXT NOT NULL,
                    valor NUMERIC
                );
            """)
            conn.commit()
            print("✅ Tabela fato_gross_up criada com sucesso no banco de testes!")

if __name__ == "__main__":
    print("🔍 Configurando o banco de testes...")
    criar_tabelas_teste()
    print("✅ Banco de testes configurado!")