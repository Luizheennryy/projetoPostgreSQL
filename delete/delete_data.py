from database.queries import execute_query
from utils.logger import delete_logger

# Função fake provisória só para permitir import e execução dos testes
def registrar_auditoria(operacao, tabela, total):
    print(f"[AUDITORIA] Operação: {operacao} | Tabela: {tabela} | Registros: {total}")

def deletar_periodo(nome_tabela, periodo):
    """Deleta registros e registra auditoria"""
    print(f"🔍 Iniciando DELETE para {nome_tabela} | Período: {periodo}")

    delete_query = f'DELETE FROM "{nome_tabela}" WHERE ano_mes = %s RETURNING *;'
    deleted_rows = execute_query(delete_query, (periodo,))
    
    print(f"⚠️ Teste: Quantidade de registros deletados: {deleted_rows}")
    
    if deleted_rows > 0:
        print(f"🔍 Chamando auditoria: DELETE {deleted_rows} registros de {nome_tabela}")
        registrar_auditoria("DELETE", nome_tabela, deleted_rows)
        print("✅ Finalizou chamada da auditoria")
    else:
        print("⚠️ Nenhuma linha foi deletada, auditoria não chamada!")
