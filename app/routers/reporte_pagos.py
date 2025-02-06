from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from typing import List
from app.models.reporte_pagos import execute_sp_reporte_pagos
from app.schemas.reporte_pagos import ReportePagosRequest, ReportePagosResponse
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/reporte-pagos", response_model=List[ReportePagosResponse], dependencies=[Security(verify_token)])
def get_reporte_pagos(data: ReportePagosRequest):
    """
    Endpoint para consumir el stored procedure SP_REPORTE_PAGOS.
    """
    try:
        result = execute_sp_reporte_pagos(data.fecha_inicio, data.fecha_fin)

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