from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas


def create(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=request.password  # TODO: need bcrypt hashing here
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user
