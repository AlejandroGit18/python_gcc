from fastapi import APIRouter, HTTPException, status
from app.models.auth import sp_login
from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    """
    Endpoint para autenticar usuarios usando SP_LOGIN.
    """
    try:
        # Llama al modelo para autenticar al usuario
        user_data = sp_login(request.username, request.password)
        
        if not user_data:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )
        
        return user_data
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
