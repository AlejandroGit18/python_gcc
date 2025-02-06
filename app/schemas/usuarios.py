from pydantic import BaseModel
from typing import Optional

# Modelo base para las operaciones
class UsuarioBase(BaseModel):
    id_rol: Optional[int]
    nombre: Optional[str]
    dpi: Optional[int]
    email: Optional[str]
    username: Optional[str]
    contraseña: Optional[str]
    fecha_nacimiento: Optional[str]
    estatus: Optional[bool]
    usuario_operacion: Optional[int]

# Modelos específicos
class UsuarioCreate(BaseModel):
    id_rol: int
    nombre: str
    dpi: int
    email: str
    username: str
    contraseña: str
    fecha_nacimiento: str
    usuario_operacion: int

class UsuarioUpdate(BaseModel):
    id_usuario: int
    id_rol: Optional[int]
    nombre: Optional[str]
    dpi: Optional[int]
    email: Optional[str]
    username: Optional[str]
    contraseña: Optional[str]
    fecha_nacimiento: Optional[str]
    usuario_operacion: int

class UsuarioToggleStatus(BaseModel):
    id_usuario: int
    estatus: bool
    usuario_operacion: int

class UsuarioSelectByID(BaseModel):
    id_usuario: int

class UsuarioSelectByStatus(BaseModel):
    estatus: bool
