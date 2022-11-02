from sqlalchemy.orm import Session

import models
import schemas
from utils import exceptions
from utils.hashutils import HashUtils


def create(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=HashUtils.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise exceptions.not_found("user not found")
    return user


def get_by_email(email: str, db: Session):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise exceptions.not_found("user not found")
    return user
