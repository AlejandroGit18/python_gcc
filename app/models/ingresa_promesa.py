from app.database import get_db_connection

def execute_sp_ingresa_promesa_pago(params: dict):
    """
    Consume el stored procedure SP_INGRESA_PROMESA_PAGO.

    :param params: Diccionario con los parámetros necesarios para el SP.
    :return: Mensaje de éxito.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_INGRESA_PROMESA_PAGO
                @P_ID_TIPOLOGIA = ?,
                @P_ID_GESTION = ?,
                @P_NO_CUENTA = ?,
                @P_CANT_CUOTAS = ?,
                @P_FECHA_PAGO = ?,
                @P_DESCUENTO = ?,
                @P_TIPO_DESCUENTO = ?,
                @P_ID_USUARIO = ?;
        """, (
            params.get("id_tipologia"),
            params.get("id_gestion"),
            params.get("no_cuenta"),
            params.get("cant_cuotas"),
            params.get("fecha_pago"),
            params.get("descuento"),
            params.get("p_descuento"),
            params.get("id_usuario"),
        ))

        connection.commit()
        return {"message": "Promesa de pago registrada exitosamente."}
    except Exception as e:
        print(f"Error executing SP_INGRESA_PROMESA_PAGO: {e}")
        raise
    finally:
        connection.close()