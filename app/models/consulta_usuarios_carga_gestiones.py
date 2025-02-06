from app.database import get_db_connection

def execute_sp_consulta_usuarios_carga_gestiones(id_campana: int):
    """
    Consume el stored procedure SP_CONSULTA_USUARIOS_CARGA_GESTIONES.

    :param id_campana: ID de la campaña para la consulta.
    :return: Resultado de la consulta.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_CONSULTA_USUARIOS_CARGA_GESTIONES @P_ID_CAMPANA = ?;
        """, (id_campana,))

        if cursor.description:  # Si hay resultados (SELECT)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result
        else:
            return []
    except Exception as e:
        print(f"Error executing SP_CONSULTA_USUARIOS_CARGA_GESTIONES: {e}")
        raise
    finally:
        connection.close()