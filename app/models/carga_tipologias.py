from app.database import get_db_connection

def execute_sp_carga_tipologia_gestiones(params: dict):
    """
    Consume el stored procedure SP_CARGA_TIPOLOGIA_GESTIONES.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Mensaje de éxito o error.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_CARGA_TIPOLOGIA_GESTIONES
                @P_ID_GESTION = ?,
                @P_TIPOGESTION = ?,
                @P_TIPOLOGIA = ?,
                @P_SUB_TIPOLOGIA = ?,
                @P_RAZON_MORA = ?,
                @P_TIPO_CONTACTO = ?,
                @P_OBSERVACIONES = ?,
                @P_INVESTIGACION = ?,
                @P_FECHA_CREACION = ?,
                @P_ID_USUARIO = ?;
        """, (
            params.get("p_id_gestion"),
            params.get("p_tipogestion"),
            params.get("p_tipologia"),
            params.get("p_sub_tipologia"),
            params.get("p_razon_mora"),
            params.get("p_tipo_contacto"),
            params.get("p_observaciones"),
            params.get("p_investigacion"),
            params.get("p_fecha_creacion"),
            params.get("p_id_usuario"),
        ))

        connection.commit()
        return {"message": "Stored procedure executed successfully."}
    except Exception as e:
        print(f"Error executing SP_CARGA_TIPOLOGIA_GESTIONES: {e}")
        raise
    finally:
        connection.close()