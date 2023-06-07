from fastapi import APIRouter,Depends
from typing import List
from .. schema import ShowUser,UserCreation
from .. database import get_db
from sqlalchemy.orm import Session
from ..views import user_apis
import math


router = APIRouter(
    prefix='/user',
    tags=["User APIs"]
)

# user creation and get apis

@router.get('/',response_model = List[ShowUser],name= "users data")
def get_uers(db:Session = Depends(get_db)):
    query = user_apis.get_user_data(db)
    return query

@router.post('/',name= "create user API",description="welcome, please signup here")
def create_user(request: UserCreation,db:Session = Depends(get_db)):
    try:
        user_data = user_apis.create_user_obj(request,db)
        return user_data
    except Exception as e:
        return {
            "message":str(e),
        }

@router.get('/hello',name= "greeting")
def greeting():
    return "Hello World"

@router.get('/teacher',name= "teacher_data")
def get_uers(db:Session = Depends(get_db)):
    query = user_apis.get_teacher_data(db)
    return query

@router.get("/distance")
def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    # Calculating the distance using the distance formula
    distance = math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
    
    return {"distance": distance}