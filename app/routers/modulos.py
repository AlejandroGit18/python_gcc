from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from app.models.modulos import (
    insert_modulo, update_modulo, update_estado_modulo, get_all_modulos, get_modulo_by_id
)
from app.schemas.modulos import (
    ModuloInsert, ModuloUpdate, ModuloUpdateEstado, ModuloResponse
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

@router.post("/modulos/insert", response_model=dict, dependencies=[Security(verify_token)])
def create_modulo(data: ModuloInsert):
    try:
        result = insert_modulo(data.dict())
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put("/modulos/update", response_model=dict, dependencies=[Security(verify_token)])
def modify_modulo(data: ModuloUpdate):
    try:
        result = update_modulo(data.dict())
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put("/modulos/update_estado", response_model=dict, dependencies=[Security(verify_token)])
def change_estado_modulo(data: ModuloUpdateEstado):
    try:
        result = update_estado_modulo(data.dict())
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/modulos", response_model=list[ModuloResponse], dependencies=[Security(verify_token)])
def get_modulos():
    try:
        result = get_all_modulos()
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/modulos/{id_modulo}", response_model=ModuloResponse, dependencies=[Security(verify_token)])
def get_modulo(id_modulo: int):
    try:
        result = get_modulo_by_id(id_modulo)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Modulo not found"
            )
        return result[0]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
