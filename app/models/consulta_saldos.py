from app.database import get_db_connection

def execute_sp_consulta_saldos(params: dict):
    """
    Consume el stored procedure SP_CONSULTA_SALDOS.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Resultado de la operación o mensaje de éxito.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_CONSULTA_SALDOS @P_ID_CAMPANA = ?;
        """, (
            params.get("id_campana"),
        ))

        if cursor.description:  # Si hay resultados (SELECT)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result
        else:
            connection.commit()
            return {"message": "Operation completed successfully"}
    except Exception as e:
        print(f"Error executing SP_CONSULTA_SALDOS: {e}")
        raise
    finally:
        connection.close()