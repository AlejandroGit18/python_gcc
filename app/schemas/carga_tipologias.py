from pydantic import BaseModel
from typing import Optional

class CargaTipologiaGestionesBase(BaseModel):
    p_id_gestion: Optional[int] = None
    p_tipogestion: Optional[str] = None
    p_tipologia: Optional[str] = None
    p_sub_tipologia: Optional[str] = None
    p_razon_mora: Optional[str] = None
    p_tipo_contacto: Optional[str] = None
    p_observaciones: Optional[str] = None
    p_investigacion: Optional[str] = None
    p_fecha_creacion: Optional[str] = None  # Formato ISO 8601
    p_id_usuario: Optional[int] = None

class CargaTipologiaGestionesResponse(BaseModel):
    message: str
    details: Optional[dict] = None