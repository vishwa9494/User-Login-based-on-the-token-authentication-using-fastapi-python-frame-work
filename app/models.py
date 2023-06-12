from .database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True',nullable=False)

    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)



class User(Base):
    __tablename__ = "users"
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)



class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
