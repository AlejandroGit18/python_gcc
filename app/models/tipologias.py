from app.database import get_db_connection

def execute_sp_carga_tipologias(params: dict):
    """
    Consume el stored procedure SP_CARGA_TIPOLOGIAS.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Resultado de la operación o mensaje de éxito.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_CARGA_TIPOLOGIAS
                @ID_CAMPANA = ?,
                @ID_USUARIO = ?,
                @P_TIPOLOGIA = ?,
                @P_SUB_TIPOLOGIA = ?,
                @P_RAZON_MORA = ?,
                @P_TIPO_CONTACTO = ?;
        """, (
            params.get("id_campana"),
            params.get("id_usuario"),
            params.get("p_tipologia"),
            params.get("p_sub_tipologia"),
            params.get("p_razon_mora"),
            params.get("p_tipo_contacto"),
        ))

        if cursor.description:  # Si hay resultados (SELECT)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result
        else:  # Operaciones como INSERT, UPDATE o DELETE
            connection.commit()
            return {"message": "Operation completed successfully"}
    except Exception as e:
        print(f"Error executing SP_CARGA_TIPOLOGIAS: {e}")
        raise
    finally:
        connection.close()