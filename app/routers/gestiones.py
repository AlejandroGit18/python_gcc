from fastapi import APIRouter, HTTPException, status, Depends, Security
from fastapi.security import OAuth2PasswordBearer
from typing import Union
from app.models.gestiones import execute_sp_crud_gestiones
from app.schemas.gestiones import (
    BaseGestion,
    GestionCrear,
    GestionActualizar,
    GestionConsultaPorId,
    GestionConsultaPorUsuarioCampana,
)
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/gestiones", response_model=Union[list[dict], dict], dependencies=[Security(verify_token)])
def crud_gestiones(data: Union[BaseGestion, GestionCrear, GestionActualizar, GestionConsultaPorId, GestionConsultaPorUsuarioCampana]):
    """
    Endpoint para realizar operaciones CRUD en TBL_GESTIONES.
    """
    try:
        params = data.dict()
        #print(f"Received data: {params}")
        opcion = params.get("opcion")  # Extrae la opción del esquema
        #print(f"Executing with opcion: {opcion}")
        result = execute_sp_crud_gestiones(params)

        if opcion in [4, 5, 6, 7]:  # Operaciones SELECT
            if not result:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No records found"
                )
            return result

        return {"message": "Operation completed successfully"}
    except Exception as e:
        if "El parámetro @P_FECHA_NACIMIENTO" in str(e):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid date of birth provided."
            )
        elif "El Usuario asignado no está disponible" in str(e):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Assigned user is not available."
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An unexpected error occurred: {str(e)}"
            )
