from pydantic import BaseModel
from typing import Optional

class IngresaTipologiaRequest(BaseModel):
    id_gestion: Optional[int] = None
    id_tipogestion: Optional[int] = None
    id_tipologia: Optional[int] = None
    id_sub_tipologia: Optional[int] = None
    id_razon_mora: Optional[int] = None
    id_tipo_contacto: Optional[int] = None
    observaciones: Optional[str] = None
    investigacion: Optional[str] = None
    id_usuario: Optional[int] = None

class IngresaTipologiaResponse(BaseModel):
    id_gestion: int