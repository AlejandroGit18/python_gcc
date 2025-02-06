from pydantic import BaseModel
from typing import Optional, List

class ConsultaTipologiasRequest(BaseModel):
    fecha_inicio: str  # ISO format YYYY-MM-DD
    fecha_fin: str  # ISO format YYYY-MM-DD

class ConsultaTipologiasResponse(BaseModel):
    TIPO_GESTION: Optional[str]
    TIPOLOGIA: Optional[str]
    SUBTIPOLOGIA: Optional[str]
    RAZON_MORA: Optional[str]
    TIPO_CONTACTO: Optional[str]
    OBSERVACIONES: Optional[str]
    INVESTIGACION: Optional[str]
    FECHA: Optional[str]
    USUARIO: Optional[str]