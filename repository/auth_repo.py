from fastapi import status, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from utils.hashutils import HashUtils


def login(request: schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")

    if not HashUtils.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
    return user
