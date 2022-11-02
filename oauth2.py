from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import database
from repository import user_repo
from utils import tokenutils

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(jwtToken: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return tokenutils.verify_token(jwtToken, credentials_exception)
