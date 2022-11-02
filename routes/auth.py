from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
import schemas
from repository import auth_repo
from utils import tokenutils

router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = auth_repo.login(request, db)
    access_token = tokenutils.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
