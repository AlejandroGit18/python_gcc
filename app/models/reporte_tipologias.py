from app.database import get_db_connection

def execute_sp_reporte_tipologias(fecha_inicio: str, fecha_fin: str):
    """
    Consume el stored procedure SP_REPORTE_TIPOLOGIAS.

    :param fecha_inicio: Fecha de inicio para el reporte.
    :param fecha_fin: Fecha de fin para el reporte.
    :return: Resultado de la consulta.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC SP_REPORTE_TIPOLOGIAS @P_FECHA_INICIO = ?, @P_FECHA_FIN = ?;
        """, (fecha_inicio, fecha_fin))

        if cursor.description:  # Si hay resultados (SELECT)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result
        else:
            return []
    except Exception as e:
        print(f"Error executing SP_REPORTE_TIPOLOGIAS: {e}")
        raise
    finally:
        connection.close()