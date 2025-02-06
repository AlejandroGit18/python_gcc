from app.database import get_db_connection

def execute_sp_crud_campanas_usuarios(params: dict):
    """
    Consume el stored procedure SP_CRUD_CAMPANAS_USUARIOS.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Resultado de la operación o lista de asociaciones.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_CRUD_CAMPANAS_USUARIOS
                @P_OPCION = ?,
                @P_ID_CAMPANA_USUARIOS = ?,
                @P_ID_CAMPANA = ?,
                @P_ID_USUARIO = ?,
                @P_ESTADO = ?,
                @P_USUARIO_OPERACION = ?;
        """, (
            params.get("opcion"),
            params.get("id_campana_usuarios"),
            params.get("id_campana"),
            params.get("id_usuario"),
            params.get("estado"),
            params.get("usuario_operacion"),
        ))

        if cursor.description:  # Si hay resultados (SELECT)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result
        else:  # Operaciones como INSERT, UPDATE o DELETE
            connection.commit()
            return {"message": "Operation completed successfully"}
    except Exception as e:
        print(f"Error executing SP_CRUD_CAMPANAS_USUARIOS: {e}")
        raise
    finally:
        connection.close()