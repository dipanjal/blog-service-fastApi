from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.orm import Session

import database
import schemas
from repository import blog_repo
from schemas import ShowBlog

router = APIRouter(
    prefix="/blogs",
    tags=['Blogs']
)

get_db = database.get_db


@router.get('/', response_model=List[ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog_repo.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog_repo.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return blog_repo.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog_repo.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog_repo.show(id, db)
