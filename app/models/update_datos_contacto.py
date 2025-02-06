from app.database import get_db_connection

def execute_sp_actualiza_informacion_contacto(params: dict):
    """
    Consume el stored procedure SP_ACTUALIZA_INFORMACION_CONTACTO.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Mensaje de éxito.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_ACTUALIZA_INFORMACION_CONTACTO
                @P_ID_GESTION = ?,
                @P_EMAIL = ?,
                @P_TELEFONO1 = ?,
                @P_TELEFONO2 = ?,
                @P_TELEFONO3 = ?,
                @P_TELEFONO4 = ?;
        """, (
            params.get("id_gestion"),
            params.get("email"),
            params.get("telefono1"),
            params.get("telefono2"),
            params.get("telefono3"),
            params.get("telefono4"),
        ))

        connection.commit()
        return {"message": "Información de contacto actualizada exitosamente."}
    except Exception as e:
        print(f"Error executing SP_ACTUALIZA_INFORMACION_CONTACTO: {e}")
        raise
    finally:
        connection.close()
