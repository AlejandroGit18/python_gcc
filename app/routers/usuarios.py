from fastapi import APIRouter, HTTPException, status, Body
from typing import Union
from app.models.usuarios import execute_sp_crud_usuarios
from app.schemas.usuarios import (
    UsuarioCreate,
    UsuarioUpdate,
    UsuarioToggleStatus,
    UsuarioSelectByID,
    UsuarioSelectByStatus,
)

router = APIRouter()

@router.post("/usuarios", response_model=Union[list[dict], dict])
def crud_usuarios(opcion: int, data: Union[UsuarioCreate, UsuarioUpdate, UsuarioToggleStatus, UsuarioSelectByID, UsuarioSelectByStatus] = Body(...)):
    """
    Endpoint para realizar operaciones CRUD en TBL_USUARIOS.
    """
    try:
        params = data.dict()
        params["opcion"] = opcion

        # Llama al procedimiento almacenado
        result = execute_sp_crud_usuarios(params)

        # Validaciones de resultado según opción
        if opcion in [4, 5, 6]:  # SELECT
            if not result:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No records found"
                )
            return result

        # Para INSERT, UPDATE, DELETE
        return {"message": "Operation completed successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
