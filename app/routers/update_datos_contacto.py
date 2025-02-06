from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from app.models.update_datos_contacto import execute_sp_actualiza_informacion_contacto
from app.schemas.update_datos_contacto import ActualizaInformacionContactoRequest, ActualizaInformacionContactoResponse
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/actualiza-informacion-contacto", response_model=ActualizaInformacionContactoResponse, dependencies=[Security(verify_token)])
def update_contact_information(data: ActualizaInformacionContactoRequest):
    """
    Endpoint para consumir el stored procedure SP_ACTUALIZA_INFORMACION_CONTACTO.
    """
    try:
        # Filtrar parámetros no utilizados
        params = {key: value for key, value in data.dict().items() if value is not None}
        result = execute_sp_actualiza_informacion_contacto(params)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
