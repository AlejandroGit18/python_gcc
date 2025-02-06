from app.database import get_db_connection

def execute_sp_crud_usuarios(params: dict):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_CRUD_USUARIOS
                @P_OPCION = ?,
                @P_ID_USUARIO = ?,
                @P_ID_ROL = ?,
                @P_NOMBRE = ?,
                @P_DPI = ?,
                @P_EMAIL = ?,
                @P_USERNAME = ?,
                @P_CONTRASEÑA = ?,
                @P_FECHA_NACIMIENTO = ?,
                @P_ESTATUS = ?,
                @P_USUARIO_OPERACION = ?;
        """, (
            params.get("opcion"),
            params.get("id_usuario"),
            params.get("id_rol"),
            params.get("nombre"),
            params.get("dpi"),
            params.get("email"),
            params.get("username"),
            params.get("contraseña"),
            params.get("fecha_nacimiento"),
            params.get("estatus"),
            params.get("usuario_operacion"),
        ))

        if cursor.description:  # Devuelve resultados
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result
        else:
            connection.commit()
            return {"message": "Operation completed successfully"}
    except Exception as e:
        print(f"Error executing stored procedure: {e}")
        raise
    finally:
        connection.close()
