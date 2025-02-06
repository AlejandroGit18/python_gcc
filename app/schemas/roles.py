from pydantic import BaseModel
from typing import Optional

class RolBase(BaseModel):
    descripcion: Optional[str]
    estatus: Optional[bool]
    usuario_operacion: Optional[int]

class RolResponse(RolBase):
    id_rol: int
    fecha_de_creacion: Optional[str]
    usuario_de_creacion: Optional[int]
    fecha_de_actualizacion: Optional[str]
    usuario_de_actualizacion: Optional[int]
