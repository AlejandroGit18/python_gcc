from pydantic import BaseModel
from typing import Optional

class IngresaPromesaPagoRequest(BaseModel):
    id_tipologia: Optional[int] = None
    id_gestion: Optional[int] = None
    no_cuenta: Optional[int] = None
    cant_cuotas: Optional[int] = None
    fecha_pago: Optional[str] = None  # ISO 8601 format (e.g., "YYYY-MM-DDTHH:MM:SS")
    descuento: Optional[float] = None
    p_descuento: Optional[str] = None
    id_usuario: Optional[int] = None

class IngresaPromesaPagoResponse(BaseModel):
    message: str