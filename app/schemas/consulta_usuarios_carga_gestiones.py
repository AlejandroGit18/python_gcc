from pydantic import BaseModel
from typing import Optional, List

class ConsultaUsuariosCargaGestionesRequest(BaseModel):
    id_campana: int

class ConsultaUsuariosCargaGestionesResponse(BaseModel):
    USERNAME: str
    NOMBRE: str