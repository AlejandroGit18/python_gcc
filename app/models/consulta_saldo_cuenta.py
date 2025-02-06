from app.database import get_db_connection

def execute_sp_consulta_saldo(id_gestion: int, cuenta: int):
    """
    Consume el stored procedure SP_CONSULTA_SALDO.

    :param id_gestion: ID de la gestion a consultar.
    :param cuenta: Número de cuenta a consultar.
    :return: Resultado de la consulta.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_CONSULTA_SALDO @P_ID_GESTION = ?, @P_CUENTA = ?;
        """, (id_gestion, cuenta))

        if cursor.description:  # Si hay resultados (SELECT)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result
        else:
            return []
    except Exception as e:
        print(f"Error executing SP_CONSULTA_SALDO: {e}")
        raise
    finally:
        connection.close()