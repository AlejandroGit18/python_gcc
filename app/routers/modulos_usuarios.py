from fastapi import APIRouter, HTTPException, status, Depends, Security
from fastapi.security import OAuth2PasswordBearer
from app.jwt_handler import JWTHandler
from app.models.modulos_usuarios import (
    insert_modulo_usuario, update_modulo_usuario, update_estado_modulo_usuario,
    get_all_modulos_usuarios, get_modulos_usuarios_by_usuario
)
from app.schemas.modulos_usuarios import (
    ModuloUsuarioInsert, ModuloUsuarioUpdate, ModuloUsuarioUpdateEstado, ModuloUsuarioResponse, ModuloUsuarioConsulta
)

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/modulos_usuarios/insert", response_model=dict, dependencies=[Security(verify_token)])
def create_modulo_usuario(data: ModuloUsuarioInsert):
    try:
        result = insert_modulo_usuario(data.dict())
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put("/modulos_usuarios/update", response_model=dict, dependencies=[Security(verify_token)])
def modify_modulo_usuario(data: ModuloUsuarioUpdate):
    try:
        result = update_modulo_usuario(data.dict())
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put("/modulos_usuarios/update_estado", response_model=dict, dependencies=[Security(verify_token)])
def change_estado_modulo_usuario(data: ModuloUsuarioUpdateEstado):
    try:
        result = update_estado_modulo_usuario(data.dict())
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/modulos_usuarios", response_model=list[ModuloUsuarioResponse], dependencies=[Security(verify_token)])
def get_modulos_usuarios():
    try:
        result = get_all_modulos_usuarios()
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/modulos_usuarios_select", response_model=list[ModuloUsuarioResponse], dependencies=[Security(verify_token)])
def get_modulo_usuario_by_usuario(data: ModuloUsuarioConsulta):
    try:
        result = get_modulos_usuarios_by_usuario(data.dict())
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="ModuloUsuarios not found for the specified user"
            )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
