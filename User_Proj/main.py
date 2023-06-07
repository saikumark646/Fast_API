from fastapi import FastAPI,Depends,status,Response,HTTPException

from .database import engine
from .import models
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash
from .routers import user,authentication

models.Base.metadata.create_all(bind=engine)  # this is manadatory to create a tables in the database

app = FastAPI()
    
app.include_router(authentication.router)
app.include_router(user.router)
