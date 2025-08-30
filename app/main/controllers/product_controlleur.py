from datetime import timedelta, datetime
from typing import Any
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.main.core.dependencies import get_db, TokenRequired
from app.main import schemas, crud, models
from app.main.core.i18n import __
from app.main.core.config import Config
from app.main.core.dependencies import TokenRequired

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/create",response_model=schemas.Msg,status_code=201)
async def create_product(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.ProductCreate
):
    exist_name = crud.product.get_by_name(db=db,name=obj_in.name)
    if exist_name:
        raise HTTPException(status_code=409, detail="this name already exist")
    crud.product.create(db=db,obj_in=obj_in)
    return schemas.Msg(message=__(key="product-created-successfully"))


@router.put("/update",response_model=schemas.Msg,status_code=200)
async def update_product(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.ProductUpdated

):
    crud.product.update(db=db,obj_in=obj_in)
    return schemas.Msg(message=__(key="product-updated-successfully"))


@router.delete("/delete",response_model=schemas.Msg,status_code=200)
async def delete_product(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.ProductDeleted,
    
):
    crud.product.delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="product-deleted-successfully"))

@router.put("/soft_delete",response_model=schemas.Msg,status_code=200)
async def soft_delete_product(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.ProductDeleted,
    
):
    crud.product.soft_delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="product-deleted-successfully"))
