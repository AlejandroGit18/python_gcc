from fastapi import APIRouter, HTTPException, status, Depends, Security
from fastapi.security import OAuth2PasswordBearer
from typing import Union
from app.models.campanas import obtener_campanas_por_usuario
from app.schemas.campanas import CampanaResponse
from app.models.campanas import execute_sp_crud_campanas
from app.schemas.campanas import CampanaBase, CampanaResponseCrud
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.get("/campanas/{id_usuario}", response_model=list[CampanaResponse], dependencies=[Security(verify_token)])
def get_campanas_por_usuario(id_usuario: int):
    """
    Endpoint para obtener campañas activas asociadas a un usuario.
    """
    try:
        result = obtener_campanas_por_usuario(id_usuario)

        if not result:  # Si no hay campañas, retorna una lista vacía
            return []

        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/campanas", response_model=Union[list[CampanaResponseCrud], dict], dependencies=[Security(verify_token)])
def crud_campanas(data: CampanaBase, opcion: int):
    """
    Endpoint para realizar operaciones CRUD en TBL_CAT_CAMPANAS.
    """
    try:
        params = data.dict()
        params["opcion"] = opcion
        result = execute_sp_crud_campanas(params)

        if opcion in [4, 5, 6]:  # Operaciones SELECT que devuelven resultados
            if not result:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No records found"
                )
            return result

        # Para operaciones como INSERT, UPDATE, DELETE
        return {"message": "Operation completed successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
