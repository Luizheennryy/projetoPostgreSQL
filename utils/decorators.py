import logging
from functools import wraps
from db import PostgreSQL

def with_db_connection(func):
    """Decorator para abrir e fechar conexões automaticamente."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = PostgreSQL.get_connection()
        try:
            return func(conn, *args, **kwargs)
        except Exception as e:
            logging.error(f"Erro na função {func.__name__}: {e}")
        finally:
            conn.close()
    return wrapper
