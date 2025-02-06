from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from typing import List
from app.models.consulta_historico_pagos import execute_sp_consulta_historico_pagos
from app.schemas.consulta_historico_pagos import ConsultaHistoricoPagosRequest, ConsultaHistoricoPagosResponse
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/consulta-historico-pagos", response_model=List[ConsultaHistoricoPagosResponse], dependencies=[Security(verify_token)])
def get_historico_pagos(data: ConsultaHistoricoPagosRequest):
    """
    Endpoint para consumir el stored procedure SP_CONSULTA_HISTORICO_PAGOS.
    """
    try:
        result = execute_sp_consulta_historico_pagos(data.id_gestion)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No records found"
            )

        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
