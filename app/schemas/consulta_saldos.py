from pydantic import BaseModel
from typing import Optional, List

class SaldosBase(BaseModel):
    id_campana: int

class SaldosResponse(BaseModel):
    ID_GESTIONES: int
    NO_CUENTA1: Optional[str]
    NO_CUENTA2: Optional[str]
    NO_CUENTA3: Optional[str]
    NO_CUENTA4: Optional[str]
    NO_CUENTA5: Optional[str]