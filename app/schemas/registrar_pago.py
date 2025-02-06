from pydantic import BaseModel
from typing import Optional

class PaymentRequest(BaseModel):
    id_gestion: Optional[int] = None
    cuenta: Optional[int] = None
    fecha_pago: Optional[str] = None  # ISO 8601 format (e.g., "YYYY-MM-DDTHH:MM:SS")
    monto_quetzales: Optional[float] = None
    monto_dolares: Optional[float] = None
    comentario: Optional[str] = None
    base64: Optional[str] = None
    id_usuario: Optional[int] = None

class PaymentResponse(BaseModel):
    message: str