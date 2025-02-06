from pydantic import BaseModel
from typing import Optional

class TipologiasBase(BaseModel):
    id_campana: Optional[int] = None
    id_usuario: Optional[int] = None
    p_tipologia: Optional[str] = None
    p_sub_tipologia: Optional[str] = None
    p_razon_mora: Optional[str] = None
    p_tipo_contacto: Optional[str] = None

class TipologiasResponse(BaseModel):
    message: str