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

router = APIRouter(prefix='/tasks')


@router.get('/')
def showall():
    pass

