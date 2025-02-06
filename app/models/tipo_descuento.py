from app.database import get_db_connection

def execute_sp_carga_tipo_descuento(params: dict):
    """
    Consume el stored procedure SP_CARGA_TIPO_DESCUENTO.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Mensaje de éxito o error.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_CARGA_TIPO_DESCUENTO
                @P_ID_CAMPANA = ?,
                @P_DESCRIPCION = ?,
                @P_DESCRIPCION1 = ?,
                @P_ID_USUARIO = ?;
        """, (
            params.get("id_campana"),
            params.get("descripcion"),
            params.get("descripcion1"),
            params.get("id_usuario"),
        ))

        connection.commit()
        return {"message": "Tipo de descuento cargado correctamente."}
    except Exception as e:
        print(f"Error executing SP_CARGA_TIPO_DESCUENTO: {e}")
        raise
    finally:
        connection.close()