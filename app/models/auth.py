from typing import Optional
from app.database import get_db_connection
from app.jwt_handler import JWTHandler  # Importa la clase para manejar JWT

jwt_handler = JWTHandler()  # Instancia de la clase para manejar JWT

def sp_login(username: str, password: str) -> Optional[dict]:
    """
    Consume el stored procedure SP_LOGIN para autenticar un usuario.
    
    :param username: Nombre de usuario
    :param password: Contraseña del usuario
    :return: Información del usuario autenticado con token JWT o None.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            EXEC [dbo].[SP_LOGIN] 
            @p_USERNAME = ?, 
            @p_CONTRASEÑA = ?;
        """, (username, password))
        
        result = cursor.fetchone()
        
        # Si el stored procedure no devuelve datos, se interpreta como un login fallido
        if not result:
            return None
        
        # Si el resultado contiene un campo 'VALIDA' con valor 0, es un login inválido
        if result[0] == 0:
            return None
        
        # Si el login es exitoso, genera un token JWT y retorna la información del usuario
        user_data = {
            "ID_USUARIO": int(result[0]),  # Convierte a entero si es necesario
            "NOMBRE": str(result[1]),
            "USERNAME": str(result[2]),
            "ID_ROL": int(result[3]),
            "ROL": str(result[4])
        }
        
        # Generar el token JWT
        token_data = {"sub": user_data["USERNAME"], "id": user_data["ID_USUARIO"]}
        user_data["token"] = jwt_handler.create_token(data=token_data)
        
        return user_data
    except Exception as e:
        print(f"Error executing SP_LOGIN: {e}")
        raise
    finally:
        connection.close()
