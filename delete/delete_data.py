from utils.decorators import with_db_connection  # Adicione essa linha
from db import PostgreSQL
from backup.backup_data import backup_dados
from psycopg2 import sql
import logging
from psycopg2 import sql

logger = logging.getLogger("delete_logger")

@with_db_connection
def deletar_periodo(conn, nome_tabelas, periodo):
    try:
        with conn.cursor() as cur:
            for tabela in nome_tabelas:
                logger.info(f"Processando DELETE para a tabela: {tabela}")
                backup_dados(conn, tabela, periodo)
                query = sql.SQL("DELETE FROM {} WHERE ano_mes LIKE %s;").format(sql.Identifier(tabela))
                cur.execute(query, (f"%{periodo}%",))
            conn.commit()
            logger.info(f"Linhas removidas com sucesso para o período {periodo}!")
    except Exception as e:
        logger.error(f"Erro ao executar DELETE: {e}")
