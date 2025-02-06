from pydantic import BaseModel
from typing import Optional, List

class ReporteTipologiasRequest(BaseModel):
    fecha_inicio: str  # ISO format YYYY-MM-DD
    fecha_fin: str  # ISO format YYYY-MM-DD

class ReporteTipologiasResponse(BaseModel):
    tipo_gestion: Optional[str]
    tipologia: Optional[str]
    subtipologia: Optional[str]
    razon_mora: Optional[str]
    tipo_contacto: Optional[str]
    observaciones: Optional[str]
    investigacion: Optional[str]
    fecha: Optional[str]
    usuario: Optional[str]
