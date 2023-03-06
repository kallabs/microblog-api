import logging
from datetime import datetime, timedelta
from typing import Union

from fastapi import Request, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from decouple import config
from passlib.context import CryptContext
from pydantic import BaseModel

logger = logging.getLogger(__name__)

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = "HS256"

class TokenData(BaseModel):
    id: int = None
    typ: int = None


class User(BaseModel):
    id: int

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/")

async def get_current_user(request: Request):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    access_token = request.headers.get('Authorization').replace('Bearer ', '')

    logger.debug('token', access_token)

    try:
        payload = jwt.decode(
            access_token, 
            SECRET_KEY, 
            algorithms=[ALGORITHM],
            options={
                "verify_signature": True,
                "verify_aud": False,
                "verify_iat": False,
                "verify_exp": False,
                "verify_nbf": False,
                "verify_iss": False,
                "verify_sub": False,
                "verify_jti": False,
                "verify_at_hash": False,
            })
        logger.debug('payload', payload)
        token_data = TokenData(id=payload.get('uid'),
                               typ=payload.get('type'))
    except JWTError:
        raise credentials_exception
    
    user = User(id=token_data.id)
    
    if user is None:
        raise credentials_exception
    
    return user
