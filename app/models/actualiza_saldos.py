from app.database import get_db_connection

def execute_sp_actualiza_saldos(params: dict):
    """
    Consume el stored procedure SP_ACTUALIZA_SALDOS.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Mensaje de éxito o error.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_ACTUALIZA_SALDOS
                @P_ID_GESTION = ?,
                @P_ID_CAMPANA = ?,
                @P_ID_USUARIO = ?,
                @P_SALDO1 = ?,
                @P_SALDO2 = ?,
                @P_SALDO3 = ?,
                @P_SALDO4 = ?,
                @P_SALDO5 = ?;
        """, (
            params.get("id_gestion"),
            params.get("id_campana"),
            params.get("id_usuario"),
            params.get("saldo1"),
            params.get("saldo2"),
            params.get("saldo3"),
            params.get("saldo4"),
            params.get("saldo5"),
        ))

        connection.commit()
        return {"message": "Balances updated successfully."}
    except Exception as e:
        print(f"Error executing SP_ACTUALIZA_SALDOS: {e}")
        raise
    finally:
        connection.close()