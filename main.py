from fastapi import FastAPI

import models
from database import engine
from routes import blog

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(blog.router)