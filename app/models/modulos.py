from app.database import get_db_connection


# Insertar
def insert_modulo(data: dict):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_TBL_CAT_MODULOS]
                @OPCION = 1,
                @ID_MODULO = NULL,
                @NOMBRE = ?,
                @IMAGEN = ?,
                @ESTADO = NULL,
                @USUARIO_CREACION = ?,
                @USUARIO_ACTUALIZACION = NULL;
        """, (data["nombre"], data.get("imagen"), data["usuario_creacion"]))

        connection.commit()
        return {"message": "Modulo inserted successfully"}
    except Exception as e:
        print(f"Error inserting modulo: {e}")
        raise
    finally:
        connection.close()


# Actualizar
def update_modulo(data: dict):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_TBL_CAT_MODULOS]
                @OPCION = 2,
                @ID_MODULO = ?,
                @NOMBRE = ?,
                @IMAGEN = ?,
                @ESTADO = NULL,
                @USUARIO_CREACION = NULL,
                @USUARIO_ACTUALIZACION = ?;
        """, (data["id_modulo"], data["nombre"], data.get("imagen"), data["usuario_actualizacion"]))

        connection.commit()
        return {"message": "Modulo updated successfully"}
    except Exception as e:
        print(f"Error updating modulo: {e}")
        raise
    finally:
        connection.close()


# Actualizar Estado
def update_estado_modulo(data: dict):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_TBL_CAT_MODULOS]
                @OPCION = 3,
                @ID_MODULO = ?,
                @NOMBRE = NULL,
                @IMAGEN = NULL,
                @ESTADO = ?,
                @USUARIO_CREACION = NULL,
                @USUARIO_ACTUALIZACION = ?;
        """, (data["id_modulo"], data["estado"], data["usuario_actualizacion"]))

        connection.commit()
        return {"message": "Estado updated successfully"}
    except Exception as e:
        print(f"Error updating estado: {e}")
        raise
    finally:
        connection.close()


# Consultar Todos
def get_all_modulos():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_TBL_CAT_MODULOS]
                @OPCION = 4,
                @ID_MODULO = NULL,
                @NOMBRE = NULL,
                @IMAGEN = NULL,
                @ESTADO = NULL,
                @USUARIO_CREACION = NULL,
                @USUARIO_ACTUALIZACION = NULL;
        """)
        columns = [col[0] for col in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return result
    except Exception as e:
        print(f"Error fetching all modulos: {e}")
        raise
    finally:
        connection.close()


# Consultar por ID
def get_modulo_by_id(id_modulo: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_TBL_CAT_MODULOS]
                @OPCION = 5,
                @ID_MODULO = ?,
                @NOMBRE = NULL,
                @IMAGEN = NULL,
                @ESTADO = NULL,
                @USUARIO_CREACION = NULL,
                @USUARIO_ACTUALIZACION = NULL;
        """, (id_modulo,))
        columns = [col[0] for col in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return result
    except Exception as e:
        print(f"Error fetching modulo by ID: {e}")
        raise
    finally:
        connection.close()
