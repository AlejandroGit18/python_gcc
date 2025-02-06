from pydantic import BaseModel
from typing import Optional

class CargaTipoDescuentoBase(BaseModel):
    id_campana: Optional[int] = None
    descripcion: Optional[str] = None
    descripcion1: Optional[str] = None
    id_usuario: Optional[int] = None

class CargaTipoDescuentoResponse(BaseModel):
    message: str