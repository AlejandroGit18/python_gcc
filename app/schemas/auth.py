from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    ID_USUARIO: int
    NOMBRE: str
    USERNAME: str
    ID_ROL: int
    ROL: str
    token: str  # Agrega el token al esquema de respuesta
