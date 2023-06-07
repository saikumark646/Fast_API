from ..models import User,Teacher
from ..hashing import Hash

def create_user_obj(request,db):
    user = User(username=request.username,password=Hash.bcrypt(request.password),email=request.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_data(db):
    data  =  db.query(User).all()
    return data

def get_teacher_data(db):
    data  =  db.query(Teacher).all()
    return data