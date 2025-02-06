from pydantic import BaseModel
from typing import Optional


# Schema para Insertar (Opción 1)
class ModuloInsert(BaseModel):
    nombre: str
    imagen: Optional[str]
    usuario_creacion: int

    class Config:
        orm_mode = True


# Schema para Actualizar (Opción 2)
class ModuloUpdate(BaseModel):
    id_modulo: int
    nombre: str
    imagen: Optional[str]
    usuario_actualizacion: int

    class Config:
        orm_mode = True


# Schema para Actualizar Estado (Opción 3)
class ModuloUpdateEstado(BaseModel):
    id_modulo: int
    estado: bool
    usuario_actualizacion: int

    class Config:
        orm_mode = True


# Schema para Consultar (Opción 4 y 5)
class ModuloResponse(BaseModel):
    id_modulo: int
    nombre: str
    imagen: Optional[str]
    estado: bool
    fecha_creacion: Optional[str]
    usuario_creacion: Optional[int]
    fecha_actualizacion: Optional[str]
    usuario_actualizacion: Optional[int]

    class Config:
        orm_mode = True
