from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Configuración de base de datos
    DB_SERVER: str = "apptualizate.cj6px0tl7fg1.us-east-2.rds.amazonaws.com"
    DB_USER: str = "Manager"
    DB_PASSWORD: str = "44Ptu4liz4t365*"
    DB_NAME: str = "COBRANZA"
    DB_PORT: int = 1433

    # Configuración de JWT 
    JWT_SECRET_KEY: str = "GCC_COBRANZA_2025_1"  
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 120  # Tiempo de expiración en minutos

    #Encryption KEY
    ENCRYPTION_KEY: str = "KEY_GCC_COBRANZA"

    class Config:
        env_file = ".env"

settings = Settings()
