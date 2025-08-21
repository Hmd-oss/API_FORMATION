from datetime import timedelta, datetime
from typing import Any
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.main.core.dependencies import get_db, TokenRequired
from app.main import schemas, crud, models
from app.main.core.i18n import __
from app.main.core.config import Config
from app.main.core.dependencies import TokenRequired

router = APIRouter(prefix="/clients", tags=["clients"])

@router.post("/create",response_model=schemas.Msg,status_code=201)
async def create_client(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.ClientCreate,
):
    exist_phone_number = crud.client.get_by_phone_number(db=db,phone_number=obj_in.phone_number)
    if exist_phone_number:
        raise HTTPException(status_code=409, detail="this phone_number already exist")
    
    exist_email = crud.client.get_by_email(db=db,email=obj_in.email)
    if exist_email:
        raise HTTPException(status_code=409, detail="this email already exist")
    
    if obj_in.phone_number2:
        exist_phone_number2=crud.client.get_by_phone_number2(db=db,phone_number2=obj_in.phone_number2)
        if exist_phone_number2:
            raise HTTPException(status_code=409, detail="this phone number already exist")
        
    crud.client.create(db=db,obj_in=obj_in)
    return schemas.Msg(message=__(key="client-created-successfully"))


@router.put("/update",response_model=schemas.Msg,status_code=200)
async def update_client(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.ClientUpdate,
):
    
    exist_phone_number = crud.client.get_by_phone_number(db=db,phone_number=obj_in.phone_number)
    if exist_phone_number:
        raise HTTPException(status_code=409, detail="this phone_number already exist")
    
    exist_email = crud.client.get_by_email(db=db,email=obj_in.email)
    if exist_email:
        raise HTTPException(status_code=409, detail="this email already exist")
    
    if obj_in.phone_number2:
        exist_phone_number2=crud.client.get_by_phone_number2(db=db,phone_number2=obj_in.phone_number2)
        if exist_phone_number2:
            raise HTTPException(status_code=409, detail="this phone number already exist")
        
    crud.client.update(db=db,obj_in=obj_in)
    return schemas.Msg(message=__(key="client-updated-successfully"))



@router.delete("/delete",response_model=schemas.Msg,status_code=200)
async def delete_client(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.ClientDelete,
    
):
    crud.client.delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="client-deleted-successfully"))


@router.put("/soft_delete",response_model=schemas.Msg,status_code=200)
async def soft_delete_client(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.ClientDelete,
    
):
    crud.client_crud.soft_delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="client-deleted-successfully"))

