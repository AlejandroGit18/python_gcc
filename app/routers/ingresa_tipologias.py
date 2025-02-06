from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from app.models.ingresa_tipologias import execute_sp_ingresa_tipologia
from app.schemas.ingresa_tipologias import IngresaTipologiaRequest, IngresaTipologiaResponse
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/ingresa-tipologia", response_model=IngresaTipologiaResponse, dependencies=[Security(verify_token)])
def insert_tipologia(data: IngresaTipologiaRequest):
    """
    Endpoint para consumir el stored procedure SP_INGRESA_TIPOLOGIA_GESTIONES.
    """
    try:
        # Filtrar parámetros no utilizados
        params = {key: value for key, value in data.dict().items() if value is not None}
        result = execute_sp_ingresa_tipologia(params)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
