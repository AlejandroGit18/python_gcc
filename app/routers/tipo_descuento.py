from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from app.models.tipo_descuento import execute_sp_carga_tipo_descuento
from app.schemas.tipo_descuento import CargaTipoDescuentoBase, CargaTipoDescuentoResponse
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/carga-tipo-descuento", response_model=CargaTipoDescuentoResponse, dependencies=[Security(verify_token)])
def carga_tipo_descuento(data: CargaTipoDescuentoBase):
    """
    Endpoint para consumir el stored procedure SP_CARGA_TIPO_DESCUENTO.
    """
    try:
        params = {key: value for key, value in data.dict().items() if value is not None}
        result = execute_sp_carga_tipo_descuento(params)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
