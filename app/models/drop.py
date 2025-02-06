from app.database import get_db_connection

def execute_sp_drops(params: dict):
    """
    Consume el stored procedure SP_DROPS.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Resultado de la operación o lista de asociaciones.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_DROPS
                @DDL = ?,
                @ID_CAMPANA = ?,
                @ID_TIPOLOGIA = ?,
                @VALOR_STRING1 = ?,
                @VALOR_STRING2 = ?,
                @VALOR_STRING3 = ?,
                @VALOR_INT1 = ?,
                @VALOR_INT2 = ?,
                @VALOR_INT3 = ?;
        """, (
            params.get("ddl"),
            params.get("id_campana"),
            params.get("id_tipologia"),
            params.get("valor_string1"),
            params.get("valor_string2"),
            params.get("valor_string3"),
            params.get("valor_int1"),
            params.get("valor_int2"),
            params.get("valor_int3"),
        ))

        if cursor.description:  # Si hay resultados (SELECT)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result
        else:  # Operaciones como INSERT, UPDATE o DELETE
            connection.commit()
            return {"message": "Operation completed successfully"}
    except Exception as e:
        print(f"Error executing SP_DROPS: {e}")
        raise
    finally:
        connection.close()
