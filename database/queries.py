from database.connection import PostgreSQLConnection

def execute_query(query, params=None, fetch=False):
    """Executa uma query SQL de forma segura"""
    conn = None
    try:
        conn = PostgreSQLConnection.get_connection()
        with conn.cursor() as cur:
            cur.execute(query, params or ())
            
            if fetch:
                result = cur.fetchall()
            else:
                result = cur.rowcount  # Retorna número de registros afetados
            
            conn.commit()
            return result
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"❌ ERRO ao executar query: {e}")
        raise
    finally:
        if conn:
            conn.close()
