from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import mode
from enum import Enum
import schemas,models
from database import SessionLocal, engine
from passlib.context import CryptContext
import hashing
from database import get_db
import oauth2
from typing import List

router = APIRouter(prefix='/tasks')


@router.get('/',response_model= List[schemas.Task],tags=['tasks'])
def showall(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks


@router.post('/',response_model=schemas.Task,tags=['tasks'])
def make(request: schemas.Task ,db: Session = Depends(get_db)):
    new_task = models.Task(name = request.name, description = request.description, priority=request.priority)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

    

