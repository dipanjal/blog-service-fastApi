from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import database
import schemas
from repository import user_repo

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return user_repo.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return user_repo.get_by_id(id, db)
