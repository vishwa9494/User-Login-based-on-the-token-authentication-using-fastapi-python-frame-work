from fastapi import FastAPI,responses,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from  psycopg2.extras import RealDictCursor 
import time
from.import models
from.import schemas,outh2
from passlib.context import CryptContext

from .database import SessionLocal,engine
from  sqlalchemy.orm import Session
from .router import user,auth,voter




pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
  




try:
    conn = psycopg2.connect(host = 'localhost',database = 'fastapi',user = 'postgres',password = 'vishwa',cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("database connection was succcesfull")
except Exception as error:
    print("connecting to database failed")
    print("Error:",error)
    time.sleep(2)

@app.get("/")
def root():
    return {"status":"hello"}


@app.get("/sqlalchemy/{id}",response_model=schemas.PostOut)
def test_post(id: int,db: Session = Depends(get_db),curent_user:int = Depends(outh2.get_current_user),limit:int = 10):
    #posts = db.query(models.Post).filter(models.Post.id == id).first()
    result = db.query(models.Post).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    print(result)
    

    return {"status": result}


@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db),curent_user:int = Depends(outh2.get_current_user),limit:int = 10,search:Optional[str]=""):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).all()
    result = db.query(models.Post).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).all()
    print(result)
    

    return {"status": result}


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.Posta,db:Session = Depends(get_db),curent_user:int = Depends(outh2.get_current_user)):
    print(curent_user.email)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    
    db.commit()
    db.refresh(new_post)   
    return {"data":new_post}


@app.delete("/vishwa/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db),curent_user:int = Depends(outh2.get_current_user)):

    post = db.query(models.Post).filter(models.Post==id)

    if post.first == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} is not found")
    
    db.commit()



    





app.include_router(user.router)
app.include_router(auth.router)
app.include_router(voter.router)


    












