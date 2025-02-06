from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from typing import List
from app.models.consulta_usuarios_carga_gestiones import execute_sp_consulta_usuarios_carga_gestiones
from app.schemas.consulta_usuarios_carga_gestiones import ConsultaUsuariosCargaGestionesRequest, ConsultaUsuariosCargaGestionesResponse
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/consulta-usuarios-carga-gestiones", response_model=List[ConsultaUsuariosCargaGestionesResponse], dependencies=[Security(verify_token)])
def get_usuarios_carga_gestiones(data: ConsultaUsuariosCargaGestionesRequest):
    """
    Endpoint para consumir el stored procedure SP_CONSULTA_USUARIOS_CARGA_GESTIONES.
    """
    try:
        result = execute_sp_consulta_usuarios_carga_gestiones(data.id_campana)

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
