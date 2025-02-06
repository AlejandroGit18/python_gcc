from pydantic import BaseModel
from typing import Optional, List

class ConsultaHistoricoPagosRequest(BaseModel):
    id_gestion: int

class ConsultaHistoricoPagosResponse(BaseModel):
    FECHA_PAGO_DMA: str
    MONTO_QUETZALES: Optional[float]
    MONTO_DOLARES: Optional[float]
    BOLETA: Optional[str]