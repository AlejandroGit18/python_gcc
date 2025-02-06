from pydantic import BaseModel
from typing import Optional, List

class ReportePagosRequest(BaseModel):
    fecha_inicio: str  # ISO format YYYY-MM-DD
    fecha_fin: str  # ISO format YYYY-MM-DD

class ReportePagosResponse(BaseModel):
    CUENTA: Optional[str]
    MONTO_QUETZALES: Optional[float]
    MONTO_DOLARES: Optional[float]
    FECHA_PAGO: Optional[str]
    FECHA_CREACION: Optional[str]
    COMENTARIOS: Optional[str]
    USUARIO: Optional[str]