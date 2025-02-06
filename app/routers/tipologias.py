from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from typing import Union
from app.models.tipologias import execute_sp_carga_tipologias
from app.schemas.tipologias import TipologiasBase, TipologiasResponse
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/tipologias", response_model=Union[TipologiasResponse, dict], dependencies=[Security(verify_token)])
def carga_tipologias(data: TipologiasBase):
    """
    Endpoint para consumir el stored procedure SP_CARGA_TIPOLOGIAS.
    """
    try:
        # Filtrar parámetros no utilizados
        params = {key: value for key, value in data.dict().items() if value is not None}
        result = execute_sp_carga_tipologias(params)

        if not result:
            return {"message": "No records found or operation completed successfully"}
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
