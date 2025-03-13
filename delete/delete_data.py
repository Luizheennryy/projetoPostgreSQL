import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
from db import PostgreSQL
from utils.logger import delete_logger

def deletar_periodo(nome_tabela, periodo):
    """Deleta registros e registra auditoria"""
    print(f"🔍 Iniciando DELETE para {nome_tabela} | Período: {periodo}")

    try:
        with PostgreSQL.get_connection() as conn:
            print(f"✅ Conexão com o banco estabelecida para {nome_tabela}")

            with conn.cursor() as cur:
                print('🚀 Iniciando a execução do script delete_data.py')
                delete_query = f'DELETE FROM "{nome_tabela}" WHERE ano_mes = %s RETURNING *;'
                print(f"📝 Executando DELETE: {delete_query} | Valores: ({periodo},)")

                cur.execute(delete_query, (periodo,))
                deleted_rows = cur.rowcount
                print(f"⚠️ Teste: Quantidade de registros deletados: {deleted_rows}")

                conn.commit()
                print("✅ DELETE executado com sucesso!")

                delete_logger.info(f"✅ DELETE executado com sucesso - Tabela: {nome_tabela} | Período: {periodo} | Registros removidos: {deleted_rows}")

                if deleted_rows > 0:
                    print(f"🔍 Chamando auditoria: DELETE {deleted_rows} registros de {nome_tabela}")
                    registrar_auditoria("DELETE", nome_tabela, deleted_rows)
                    print("✅ Finalizou chamada da auditoria")
                else:
                    print("⚠️ Nenhuma linha foi deletada, auditoria não chamada!")

    except Exception as e:
        conn.rollback()
        print(f"❌ ERRO ao deletar da tabela {nome_tabela}: {e}")
        delete_logger.error(f"❌ ERRO ao deletar da tabela {nome_tabela}: {e}")
        raise

def registrar_auditoria(operacao, nome_tabela, registros_afetados):
    """Insere um registro de auditoria no banco"""
    try:
        print(f"🔍 Registrando auditoria: {operacao} | Tabela: {nome_tabela} | Registros: {registros_afetados}")
        
        with PostgreSQL.get_connection() as conn:
            with conn.cursor() as cur:
                query = """
                    INSERT INTO log_auditoria (operacao, tabela_afetada, registros_afetados)
                    VALUES (%s, %s, %s);
                """
                print(f"📝 Executando SQL: {query} | Valores: ({operacao}, {nome_tabela}, {registros_afetados})")

                cur.execute(query, (operacao, nome_tabela, registros_afetados))
                
                conn.commit()  # 🔥 Forçando o commit
                print("✅ Auditoria registrada com sucesso!")

    except Exception as e:
        delete_logger.error(f"❌ ERRO ao registrar auditoria: {e}")
        print(f"❌ ERRO ao registrar auditoria: {e}")

if __name__ == "__main__":
    print("🚀 Iniciando a execução do script delete_data.py")
    deletar_periodo("Fato_UR", "2025-03")  # Teste com uma tabela de exemplo
