from fastapi import APIRouter, HTTPException, Depends, Security, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from cryptography.fernet import Fernet
from app.config import settings
from app.jwt_handler import JWTHandler
import base64

router = APIRouter()

# Initialize JWT handler
jwt_handler = JWTHandler()

# Define OAuth2 Bearer token dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Initialize Fernet encryption key from settings
encryption_key = base64.urlsafe_b64encode(settings.ENCRYPTION_KEY.ljust(32).encode())
fernet = Fernet(encryption_key)

# Schemas
class EncryptRequest(BaseModel):
    value: str

class DecryptRequest(BaseModel):
    encrypted_value: str

# Utility function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    return jwt_handler.verify_token(token)

# Routes
@router.post("/encrypt", dependencies=[Security(verify_token)])
def encrypt(data: EncryptRequest):
    """
    Encrypts a given value using Fernet encryption.
    Requires a valid Bearer token.
    """
    try:
        encrypted_value = fernet.encrypt(data.value.encode()).decode()
        return {"encrypted_value": encrypted_value}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Encryption failed") from e

@router.post("/decrypt", dependencies=[Security(verify_token)])
def decrypt(data: DecryptRequest):
    """
    Decrypts a given encrypted value using Fernet encryption.
    Requires a valid Bearer token.
    """
    try:
        decrypted_value = fernet.decrypt(data.encrypted_value.encode()).decode()
        return {"decrypted_value": decrypted_value}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Decryption failed. Invalid input or key.") from e
