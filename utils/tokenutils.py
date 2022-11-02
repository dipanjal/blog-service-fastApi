from datetime import datetime, timedelta
from jose import JWTError, jwt

import config
import schemas

ALGORITHM = "HS256"
jwt_config = config.JWTSettings()


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=jwt_config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, jwt_config.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, jwt_config.SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        id: int = payload.get("id")
        if email is None or id is None:
            raise credentials_exception
        return schemas.CurrentUser(email=email, id=id)
    except JWTError:
        raise credentials_exception
