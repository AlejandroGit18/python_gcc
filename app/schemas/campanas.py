from pydantic import BaseModel
from typing import Optional

class CampanaResponse(BaseModel):
    id_campana: int
    nombre: str
    imagen: str
    estado: bool

class CampanaBase(BaseModel):
    nombre: Optional[str]
    imagen: Optional[str]
    estado: Optional[bool]
    usuario_operacion: Optional[int]

class CampanaResponseCrud(CampanaBase):
    id_campana: int
    fecha_creacion: Optional[str]
    usuario_creacion: Optional[int]
    fecha_actualizacion: Optional[str]
    usuario_actualizacion: Optional[int]

