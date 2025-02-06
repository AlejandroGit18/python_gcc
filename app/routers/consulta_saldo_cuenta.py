from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from typing import List
from app.models.consulta_saldo_cuenta import execute_sp_consulta_saldo
from app.schemas.consulta_saldo_cuenta import ConsultaSaldoRequest, ConsultaSaldoResponse
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/consulta-saldo-cuenta", response_model=List[ConsultaSaldoResponse], dependencies=[Security(verify_token)])
def get_consulta_saldo(data: ConsultaSaldoRequest):
    """
    Endpoint para consumir el stored procedure SP_CONSULTA_SALDO.
    """
    try:
        result = execute_sp_consulta_saldo(data.id_gestion, data.cuenta)

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
