from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from typing import List
from app.models.consulta_saldos import execute_sp_consulta_saldos
from app.schemas.consulta_saldos import SaldosBase, SaldosResponse
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/consulta-saldos", response_model=List[SaldosResponse], dependencies=[Security(verify_token)])
def consulta_saldos(data: SaldosBase):
    """
    Endpoint para consumir el stored procedure SP_CONSULTA_SALDOS.
    """
    try:
        params = {key: value for key, value in data.dict().items() if value is not None}
        result = execute_sp_consulta_saldos(params)

        if not result:
            return []
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
