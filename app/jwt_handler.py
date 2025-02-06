from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException, status
from app.config import settings


class JWTHandler:
    """
    Clase para manejar la lógica de creación y verificación de JWT.
    """
    def __init__(self):
        self.secret_key = settings.JWT_SECRET_KEY
        self.algorithm = settings.JWT_ALGORITHM
        self.expire_minutes = settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES

    def create_token(self, data: dict) -> str:
        """
        Genera un token JWT.
        :param data: Diccionario con la información a incluir en el payload.
        :return: Token JWT.
        """
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.expire_minutes)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def verify_token(self, token: str) -> dict:
        """
        Verifica un token JWT.
        :param token: Token JWT a verificar.
        :return: Payload decodificado si el token es válido.
        :raises: HTTPException si el token es inválido o ha expirado.
        """
        try:
            decoded_token = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )
