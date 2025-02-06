from app.database import get_db_connection


# Insertar (Opción 1)
def insert_modulo_usuario(data: dict):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_TBL_MODULOS_USUARIOS]
                @OPCION = 1,
                @ID_MODULO_USUARIOS = NULL,
                @ID_MODULO = ?,
                @ID_USUARIO = ?,
                @ESTADO = NULL,
                @USUARIO_CREACION = ?,
                @USUARIO_ACTUALIZACION = NULL,
                @ID_CAMPANA = ?;
        """, (data["id_modulo"], data["id_usuario"], data["usuario_creacion"], data["id_campana"]))

        connection.commit()
        return {"message": "ModuloUsuario inserted successfully"}
    except Exception as e:
        print(f"Error inserting ModuloUsuario: {e}")
        raise
    finally:
        connection.close()


# Actualizar (Opción 2)
def update_modulo_usuario(data: dict):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_TBL_MODULOS_USUARIOS]
                @OPCION = 2,
                @ID_MODULO_USUARIOS = ?,
                @ID_MODULO = ?,
                @ID_USUARIO = ?,
                @ESTADO = NULL,
                @USUARIO_CREACION = NULL,
                @USUARIO_ACTUALIZACION = ?,
                @ID_CAMPANA = ?;
        """, (data["id_modulo_usuarios"], data["id_modulo"], data["id_usuario"], data["usuario_actualizacion"], data["id_campana"]))

        connection.commit()
        return {"message": "ModuloUsuario updated successfully"}
    except Exception as e:
        print(f"Error updating ModuloUsuario: {e}")
        raise
    finally:
        connection.close()


# Actualizar Estado (Opción 3)
def update_estado_modulo_usuario(data: dict):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_TBL_MODULOS_USUARIOS]
                @OPCION = 3,
                @ID_MODULO_USUARIOS = ?,
                @ID_MODULO = NULL,
                @ID_USUARIO = NULL,
                @ESTADO = ?,
                @USUARIO_CREACION = NULL,
                @USUARIO_ACTUALIZACION = ?;
        """, (data["id_modulo_usuarios"], data["estado"], data["usuario_actualizacion"]))

        connection.commit()
        return {"message": "Estado updated successfully"}
    except Exception as e:
        print(f"Error updating estado: {e}")
        raise
    finally:
        connection.close()


# Consultar Todos (Opción 4)
def get_all_modulos_usuarios():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_TBL_MODULOS_USUARIOS]
                @OPCION = 4,
                @ID_MODULO_USUARIOS = NULL,
                @ID_MODULO = NULL,
                @ID_USUARIO = NULL,
                @ESTADO = NULL,
                @USUARIO_CREACION = NULL,
                @USUARIO_ACTUALIZACION = NULL;
        """)
        columns = [col[0] for col in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return result
    except Exception as e:
        print(f"Error fetching all ModuloUsuarios: {e}")
        raise
    finally:
        connection.close()


# Consultar por Usuario (Opción 5)
def get_modulos_usuarios_by_usuario(data: dict):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_TBL_MODULOS_USUARIOS]
                @OPCION = 5,
                @ID_MODULO_USUARIOS = NULL,
                @ID_MODULO = NULL,
                @ID_USUARIO = ?,
                @ID_CAMPANA = ?,
                @ESTADO = NULL,
                @USUARIO_CREACION = NULL,
                @USUARIO_ACTUALIZACION = NULL;
        """, (data["id_usuario"],data["id_campana"]))
        
        columns = [col[0] for col in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return result
    except Exception as e:
        print(f"Error fetching ModuloUsuarios by usuario: {e}")
        raise
    finally:
        connection.close()
