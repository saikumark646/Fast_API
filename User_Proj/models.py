from .database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlmodel import DateTime, Field, Relationship, SQLModel, Column, JSON
from pydantic import EmailStr
from sqlalchemy.orm import relationship


class Blog(Base):                  
    __tablename__= "blogs"
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'))
    # creator = relationship("User",back_populates="User")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String)
    password = Column(String)   # to hash the password use install passlib
    email = Column(String)
    teacher = relationship("Teacher", back_populates="teac")
    student = relationship("Student", back_populates="std")
    # blogs = relationship("Blog",back_populates="creator")

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True,index=True)
    user = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    teac = relationship("User", back_populates="teacher")

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True,index=True)
    user = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    std = relationship("User", back_populates="student")
