from pydantic import BaseModel
from typing import Optional, List

class ReportePromesasRequest(BaseModel):
    fecha_inicio: str  # ISO format YYYY-MM-DD
    fecha_fin: str  # ISO format YYYY-MM-DD

class ReportePromesasResponse(BaseModel):
    CUENTA: Optional[str]
    CANT_CUOTAS: Optional[int]
    FECHA_PAGO: Optional[str]
    DESCUENTO: Optional[float]
    TIPO_DESCUENTO: Optional[str]
    FECHA_CREACION: Optional[str]
    TIPO_GESTION: Optional[str]
    TIPOLOGIA: Optional[str]
    SUBTIPOLOGIA: Optional[str]
    RAZON_MORA: Optional[str]
    TIPO_CONTACTO: Optional[str]
    OBSERVACIONES: Optional[str]
    INVESTIGACION: Optional[str]
    USUARIO: Optional[str]
