from pydantic import BaseModel
from typing import Optional

class ConsultaSaldoRequest(BaseModel):
    id_gestion: int
    cuenta: int

class ConsultaSaldoResponse(BaseModel):
    CUENTA: Optional[float]