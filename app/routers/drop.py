from fastapi import APIRouter, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer
from typing import Union
from app.models.drop import execute_sp_drops
from app.schemas.drop import DropsBase, DropsResponse
from app.jwt_handler import JWTHandler

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

@router.post("/drops", response_model=Union[list[DropsResponse], dict], dependencies=[Security(verify_token)])
def get_drops(data: DropsBase):
    """
    Endpoint para consumir el stored procedure SP_DROPS.
    """
    try:
        # Filtrar parámetros no utilizados
        params = {key: value for key, value in data.dict().items() if value is not None}
        result = execute_sp_drops(params)

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
