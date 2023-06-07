from fastapi import APIRouter,Depends
from .. database import get_db
from sqlalchemy.orm import Session
from ..models import User
from ..hashing import Hash
from ..token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(get_db)): 
    query = db.query(User).filter(User.email == request.username).first()
    if not (query and Hash.verify(query.password,request.password)):  
        data =  {"message":"Please enter your email and password correctly"}
    else:
        access_token = create_access_token(
            data={"sub": query.email}
        )
        data = {"result":query,
                 "message":"authenticated_successfully",
                 "access_token":access_token}
    return data