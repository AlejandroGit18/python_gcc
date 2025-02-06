from fastapi import APIRouter, HTTPException, status
from app.models.roles import execute_sp_crud_roles
from app.schemas.roles import RolBase, RolResponse

router = APIRouter()

@router.post("/roles", response_model=list[RolResponse])
def crud_roles(data: RolBase, opcion: int):
    """
    Endpoint para realizar operaciones CRUD en TBL_CAT_ROLES.
    """
    try:
        params = data.dict()
        params["opcion"] = opcion
        result = execute_sp_crud_roles(params)

        if opcion in [4, 5, 6]:  # Operaciones que devuelven resultados (SELECT)
            if not result:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No records found"
                )
            return result

        # Para operaciones como INSERT o UPDATE, retorna un mensaje
        return []
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
