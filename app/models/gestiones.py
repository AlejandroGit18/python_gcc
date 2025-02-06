from app.database import get_db_connection

def execute_sp_crud_gestiones(params: dict):
    """
    Ejecuta el procedimiento almacenado SP_CRUD_GESTIONES.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Resultado del SP (lista o mensaje de éxito).
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        #print(f"Executing SP with params: {params}")
        #print(f"Executing SP with option: {params.get("opcion")}")
        cursor.execute("""
            EXEC SP_CRUD_GESTIONES
                @P_OPCION = ?,
                @P_ID_GESTIONES = ?,
                @P_ID_CAMPANA = ?,
                @P_ID_DEUDOR = ?,
                @P_USUARIO = ?,
                @P_ID_USUARIO = ?,
                @P_NOMBRE = ?,
                @P_DIRECCION_CASA = ?,
                @P_DIRECCION_TRABAJO = ?,
                @P_LUGAR_TRABAJO = ?,
                @P_EMAIL = ?,
                @P_NIT = ?,
                @P_FECHA_NACIMIENTO = ?,
                @P_DPI = ?,
                @P_TELEFONO_CELULAR = ?,
                @P_TELEFONO_CASA = ?,
                @P_TELEFONO_ALTERNO = ?,
                @P_TELEFONO_TRABAJO = ?,
                @P_TIPO_CUENTA1 = ?,
                @P_NO_CUENTA1 = ?,
                @P_SALDO1 = ?,
                @P_TIPO_CUENTA2 = ?,
                @P_NO_CUENTA2 = ?,
                @P_SALDO2 = ?,
                @P_TIPO_CUENTA3 = ?,
                @P_NO_CUENTA3 = ?,
                @P_SALDO3 = ?,
                @P_TIPO_CUENTA4 = ?,
                @P_NO_CUENTA4 = ?,
                @P_SALDO4 = ?,
                @P_TIPO_CUENTA5 = ?,
                @P_NO_CUENTA5 = ?,
                @P_SALDO5 = ?,
                @P_CONCEPTO1 = ?,
                @P_DESCRIPCION1 = ?,
                @P_CONCEPTO2 = ?,
                @P_DESCRIPCION2 = ?,
                @P_CONCEPTO3 = ?,
                @P_DESCRIPCION3 = ?,
                @P_CONCEPTO4 = ?,
                @P_DESCRIPCION4 = ?,
                @P_ESTADO = ?,
                @P_USUARIO_OPERACION = ?;
        """, (
            params.get("opcion"),
            params.get("id_gestiones"),
            params.get("id_campana"),
            params.get("id_deudor"),
            params.get("usuario"),
            params.get("id_usuario"),
            params.get("nombre"),
            params.get("direccion_casa"),
            params.get("direccion_trabajo"),
            params.get("lugar_trabajo"),
            params.get("email"),
            params.get("nit"),
            params.get("fecha_nacimiento"),
            params.get("dpi"),
            params.get("telefono_celular"),
            params.get("telefono_casa"),
            params.get("telefono_alterno"),
            params.get("telefono_trabajo"),
            params.get("tipo_cuenta1"),
            params.get("no_cuenta1"),
            params.get("saldo1"),
            params.get("tipo_cuenta2"),
            params.get("no_cuenta2"),
            params.get("saldo2"),
            params.get("tipo_cuenta3"),
            params.get("no_cuenta3"),
            params.get("saldo3"),
            params.get("tipo_cuenta4"),
            params.get("no_cuenta4"),
            params.get("saldo4"),
            params.get("tipo_cuenta5"),
            params.get("no_cuenta5"),
            params.get("saldo5"),
            params.get("concepto1"),
            params.get("descripcion1"),
            params.get("concepto2"),
            params.get("descripcion2"),
            params.get("concepto3"),
            params.get("descripcion3"),
            params.get("concepto4"),
            params.get("descripcion4"),
            params.get("estado"),
            params.get("usuario_operacion"),
        ))

        if cursor.description:
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            #print(f"Raw rows: {rows}")
            result = [dict(zip(columns, row)) for row in rows]
            #print(f"Processed result: {result}")
            return result
        else:  # Operaciones INSERT, UPDATE o DELETE
            connection.commit()
            print("SP executed successfully")
            return {"message": "Operation completed successfully"}
    except Exception as e:
        print(f"Error executing SP_CRUD_GESTIONES: {e}")
        raise
    finally:
        connection.close()
