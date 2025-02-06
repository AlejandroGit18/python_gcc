from app.database import get_db_connection

def execute_sp_ingresa_pagos(params: dict):
    """
    Consume el stored procedure SP_INGRESA_PAGOS.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Mensaje de éxito o error.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_INGRESA_PAGOS
                @P_ID_GESTION = ?,
                @P_CUENTA = ?,
                @P_FECHA_PAGO = ?,
                @P_MONTO_QUETZALES = ?,
                @P_MONTO_DOLARES = ?,
                @P_COMENTARIO = ?,
                @P_BASE64 = ?,
                @P_ID_USUARIO = ?;
        """, (
            params.get("id_gestion"),
            params.get("cuenta"),
            params.get("fecha_pago"),
            params.get("monto_quetzales"),
            params.get("monto_dolares"),
            params.get("comentario"),
            params.get("base64"),
            params.get("id_usuario"),
        ))

        connection.commit()
        return {"message": "Payment successfully registered."}
    except Exception as e:
        print(f"Error executing SP_INGRESA_PAGOS: {e}")
        raise
    finally:
        connection.close()