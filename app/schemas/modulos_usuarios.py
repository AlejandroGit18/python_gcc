from pydantic import BaseModel
from typing import Optional


# Schema para Insertar (Opción 1)
class ModuloUsuarioInsert(BaseModel):
    id_modulo: int
    id_usuario: int
    usuario_creacion: int
    id_campana: int

    class Config:
        orm_mode = True


# Schema para Actualizar (Opción 2)
class ModuloUsuarioUpdate(BaseModel):
    id_modulo_usuarios: int
    id_modulo: int
    id_usuario: int
    id_campana: int
    usuario_actualizacion: int

    class Config:
        orm_mode = True


# Schema para Actualizar Estado (Opción 3)
class ModuloUsuarioUpdateEstado(BaseModel):
    id_modulo_usuarios: int
    estado: bool
    usuario_actualizacion: int

    class Config:
        orm_mode = True

# Schema para Actualizar Estado (Opción 3)
class ModuloUsuarioConsulta(BaseModel):
    id_usuario: int
    id_campana: int
    
    class Config:
        orm_mode = True


# Schema para Consultar (Opción 4 y 5)
class ModuloUsuarioResponse(BaseModel):
    ID_MODULO: int
    NOMBRE: str
    IMAGEN: str
    #estado: bool

    class Config:
        orm_mode = True
