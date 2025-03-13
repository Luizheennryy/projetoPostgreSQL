import logging
from psycopg2 import sql

logging.basicConfig(filename="logs/delete_process.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def backup_dados(conn, tabela, periodo):
    """Cria um backup antes da exclusão."""
    try:
        with conn.cursor() as cur:
            backup_table = f"{tabela}_backup"
            
            # Criando a tabela de backup sem erro de sintaxe
            create_backup_query = sql.SQL("""
                CREATE TABLE IF NOT EXISTS {} AS TABLE {} WITH NO DATA;
            """).format(
                sql.Identifier(backup_table), 
                sql.Identifier(tabela)
            )

            insert_backup_query = sql.SQL("""
                INSERT INTO {} SELECT * FROM {} WHERE ano_mes LIKE %s;
            """).format(
                sql.Identifier(backup_table), 
                sql.Identifier(tabela)
            )

            cur.execute(create_backup_query)
            cur.execute(insert_backup_query, (f"%{periodo}%",))

            # ✅ Corrigindo erro de sintaxe no log
            logging.info(f"✅ Backup realizado para a tabela {tabela} - Período: {periodo}")

    except Exception as e:
        logging.error(f"❌ Erro ao criar backup para {tabela}: {e}")
