from pydantic import BaseModel
from typing import Optional

class CampanaUsuarioBase(BaseModel):
    id_campana: Optional[int]
    id_usuario: Optional[int]
    estado: Optional[bool]
    usuario_operacion: Optional[int]

class CampanaUsuarioResponse(CampanaUsuarioBase):
    id_campana_usuarios: int
    fecha_creacion: Optional[str]
    usuario_creacion: Optional[int]
    fecha_actualizacion: Optional[str]
    usuario_actualizacion: Optional[int]