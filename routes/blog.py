from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import database
import oauth2
import schemas
from repository import blog_repo

router = APIRouter(
    prefix="/blogs",
    tags=['Blogs']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(database.get_db)):
    return blog_repo.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_by_id(id: int, db: Session = Depends(database.get_db), current_user: schemas.CurrentUser = Depends(oauth2.get_current_user)):
    return blog_repo.get_by_id(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.CurrentUser = Depends(oauth2.get_current_user)):
    return blog_repo.create(request, current_user.id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.CurrentUser = Depends(oauth2.get_current_user)):
    return blog_repo.delete(id, current_user.id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.CurrentUser = Depends(oauth2.get_current_user)):
    return blog_repo.update(id, request, current_user.id, db)
