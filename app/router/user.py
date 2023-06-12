from .. import models,schemas,utils
from fastapi import FastAPI,responses,status,HTTPException,Depends,APIRouter
from  sqlalchemy.orm import Session
from .. database import get_db
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")



router = APIRouter( prefix="/users" )







@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate,db:Session = Depends(get_db)):

    hashes_password = pwd_context.hash(user.password)
    user.password = hashes_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"data":new_user}




@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id : int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")
    return user



