from pydantic import BaseModel
from typing import Optional

class ActualizaInformacionContactoRequest(BaseModel):
    id_gestion: int
    email: Optional[str] = None
    telefono1: Optional[str] = None
    telefono2: Optional[str] = None
    telefono3: Optional[str] = None
    telefono4: Optional[str] = None

class ActualizaInformacionContactoResponse(BaseModel):
    message: str