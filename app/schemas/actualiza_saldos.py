from pydantic import BaseModel
from typing import Optional

class ActualizaSaldosBase(BaseModel):
    id_gestion: int
    id_campana: int
    id_usuario: int
    saldo1: Optional[float] = None
    saldo2: Optional[float] = None
    saldo3: Optional[float] = None
    saldo4: Optional[float] = None
    saldo5: Optional[float] = None

class ActualizaSaldosResponse(BaseModel):
    message: str