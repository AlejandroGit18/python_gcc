from app.database import get_db_connection

def execute_sp_ingresa_tipologia(params: dict):
    """
    Consume el stored procedure SP_INGRESA_TIPOLOGIA_GESTIONES.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: ID de la gestión insertada.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_INGRESA_TIPOLOGIA_GESTIONES
                @P_ID_GESTION = ?,
                @P_ID_TIPOGESTION = ?,
                @P_ID_TIPOLOGIA = ?,
                @P_ID_SUB_TIPOLOGIA = ?,
                @P_ID_RAZON_MORA = ?,
                @P_ID_TIPO_CONTACTO = ?,
                @P_OBSERVACIONES = ?,
                @P_INVESTIGACION = ?,
                @P_ID_USUARIO = ?;
        """, (
            params.get("id_gestion"),
            params.get("id_tipogestion"),
            params.get("id_tipologia"),
            params.get("id_sub_tipologia"),
            params.get("id_razon_mora"),
            params.get("id_tipo_contacto"),
            params.get("observaciones"),
            params.get("investigacion"),
            params.get("id_usuario"),
        ))

        id_gestion = cursor.fetchone()[0]  # Obtiene el ID de la gestión insertada
        connection.commit()
        return {"id_gestion": id_gestion}
    except Exception as e:
        print(f"Error executing SP_INGRESA_TIPOLOGIA_GESTIONES: {e}")
        raise
    finally:
        connection.close()