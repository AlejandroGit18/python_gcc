from app.database import get_db_connection

def obtener_campanas_por_usuario(id_usuario: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_OBTENER_CAMPANAS_POR_USUARIO] @ID_USUARIO = ?;
        """, (id_usuario,))
        
        if cursor.description:
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            
            # Transformar nombres y tipos
            result = [
                {
                    "id_campana": int(row["ID_CAMPANA"]),
                    "nombre": row["NOMBRE"],
                    "imagen": row["IMAGEN"],
                    "estado": row["ESTADO"]
                }
                for row in result
            ]
            return result
        else:
            return []
    except Exception as e:
        print(f"Error executing stored procedure: {e}")
        raise
    finally:
        connection.close()

def execute_sp_crud_campanas(params: dict):
    """
    Consume el stored procedure SP_CRUD_CAMPANAS para realizar operaciones CRUD.

    :param params: Diccionario con los parámetros necesarios.
    :return: Resultado de la operación o lista de campañas.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_CRUD_CAMPANAS
                @P_OPCION = ?,
                @P_ID_CAMPANA = ?,
                @P_NOMBRE = ?,
                @P_IMAGEN = ?,
                @P_ESTADO = ?,
                @P_USUARIO_OPERACION = ?;
        """, (
            params.get("opcion"),
            params.get("id_campana"),
            params.get("nombre"),
            params.get("imagen"),
            params.get("estado"),
            params.get("usuario_operacion"),
        ))

        if cursor.description:  # Si hay resultados (SELECT)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result
        else:  # Para operaciones INSERT, UPDATE o DELETE
            connection.commit()
            return {"message": "Operation completed successfully"}
    except Exception as e:
        print(f"Error executing SP_CRUD_CAMPANAS: {e}")
        raise
    finally:
        connection.close()

