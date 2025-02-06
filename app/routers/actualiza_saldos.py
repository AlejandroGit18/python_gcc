from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from app.models.actualiza_saldos import execute_sp_actualiza_saldos
from app.schemas.actualiza_saldos import ActualizaSaldosBase, ActualizaSaldosResponse
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/actualiza-saldos", response_model=ActualizaSaldosResponse, dependencies=[Security(verify_token)])
def actualiza_saldos(data: ActualizaSaldosBase):
    """
    Endpoint para consumir el stored procedure SP_ACTUALIZA_SALDOS.
    """
    try:
        params = {key: value for key, value in data.dict().items() if value is not None}
        result = execute_sp_actualiza_saldos(params)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
