from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import database
from repository import auth_repo
from utils import tokenutils

router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = auth_repo.login(request, db)
    access_token = tokenutils.create_access_token({
            "sub": user.email,
            "id": user.id
    })
    return {"access_token": access_token, "token_type": "bearer"}
