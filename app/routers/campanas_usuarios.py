from fastapi import APIRouter, HTTPException, status
from typing import Union
from app.models.campanas_usuarios import execute_sp_crud_campanas_usuarios
from app.schemas.campanas_usuarios import CampanaUsuarioBase, CampanaUsuarioResponse

router = APIRouter()

@router.post("/campanas_usuarios", response_model=Union[list[CampanaUsuarioResponse], dict])
def crud_campanas_usuarios(data: CampanaUsuarioBase, opcion: int):
    """
    Endpoint para realizar operaciones CRUD en TBL_CAMPANAS_USUARIOS.
    """
    try:
        params = data.dict()
        params["opcion"] = opcion
        result = execute_sp_crud_campanas_usuarios(params)

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