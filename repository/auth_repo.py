from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import models
from utils import exceptions
from utils.hashutils import HashUtils


def login(request: OAuth2PasswordRequestForm, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise exceptions.not_found("invalid credentials")
    if not HashUtils.verify(user.password, request.password):
        raise exceptions.not_found("incorrect password")
    return user
