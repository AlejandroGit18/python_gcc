from pydantic import BaseModel
from typing import Optional

class DropsBase(BaseModel):
    ddl: Optional[str]
    id_campana: Optional[int] = None
    id_tipologia: Optional[int] = None
    valor_string1: Optional[str] = None
    valor_string2: Optional[str] = None
    valor_string3: Optional[str] = None
    valor_int1: Optional[int] = None
    valor_int2: Optional[int] = None
    valor_int3: Optional[int] = None

class DropsResponse(BaseModel):
    VALUE: Optional[int]
    ITEM: Optional[str]
