from app.database import get_db_connection

def execute_sp_consulta_historico_pagos(id_gestion: int):
    """
    Consume el stored procedure SP_CONSULTA_HISTORICO_PAGOS.

    :param id_gestion: ID de la gestión para consultar el histórico de pagos.
    :return: Resultado de la consulta.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_CONSULTA_HISTORICO_PAGOS @P_ID_GESTION = ?;
        """, (id_gestion,))

        if cursor.description:  # Si hay resultados (SELECT)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result
        else:
            return []
    except Exception as e:
        print(f"Error executing SP_CONSULTA_HISTORICO_PAGOS: {e}")
        raise
    finally:
        connection.close()