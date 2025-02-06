from app.database import get_db_connection

def execute_sp_crud_roles(params: dict):
    """
    Consume el stored procedure SP_CRUD_ROLES para gestionar roles.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Resultado de la operación o datos obtenidos.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_CRUD_ROLES
                @P_OPCION = ?,
                @P_ID_ROL = ?,
                @P_DESCRIPCION = ?,
                @P_ESTATUS = ?,
                @P_USUARIO_OPERACION = ?;
        """, (
            params.get("opcion"),
            params.get("id_rol"),
            params.get("descripcion"),
            params.get("estatus"),
            params.get("usuario_operacion"),
        ))

        if cursor.description:  # Devuelve resultados (por ejemplo SELECT)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result
        else:  # Operaciones como INSERT, UPDATE o DELETE
            connection.commit()
            return {"message": "Operation completed successfully"}
    except Exception as e:
        print(f"Error executing stored procedure: {e}")
        raise
    finally:
        connection.close()
