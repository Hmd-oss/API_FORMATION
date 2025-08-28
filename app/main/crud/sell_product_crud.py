import math
import bcrypt
from fastapi import HTTPException
from sqlalchemy import or_
import re
from typing import List, Optional, Union
import uuid
from app.main.core.i18n import __
from sqlalchemy.orm import Session
from app.main.crud.base import CRUDBase
from app.main import models,schemas

class CRUDsell_product(CRUDBase[models.SellProduct,schemas.SellProductCreate,schemas.SellProductUpdate]):

    @classmethod
    def get_by_uuid(cls,db:Session,uuid:str):
        return db.query(models.SellProduct).filter(models.SellProduct.uuid==uuid,models.SellProduct.is_deleted==False).first()
    
    @classmethod
    def get_by_client(cls,db:Session,client:str):
        return db.query(models.SellProduct).filter(models.SellProduct.client_uuid==client,models.SellProduct.is_deleted==False).first()
    
    @classmethod
    def delete(cls,db:Session,uuid:str):
        db_obj=cls.get_by_uuid(db=db,uuid=uuid)
        if not db_obj:
            raise HTTPException(status_code=404,detail="product sold not found")
        db.delete(db_obj)
        db.commit()

    @classmethod
    def soft_delete(cls,db:Session,uuid:str):
        db_obj = cls.get_by_uuid(db==db,uuid==uuid)
        if not db_obj:
            raise HTTPException(status_code=404,detail="product_sold not found")
        db_obj.is_deleted=True
        db.commit()

    @classmethod
    def create(cls,db:Session,obj_in:schemas.SellProductCreate,added_by:str):
        db_obj=models.SellProduct(
            uuid=str(uuid.uuid4()),
            client_uuid=obj_in.client_uuid,
            product_uuid = obj_in.product_uuid,
            qte_sell = obj_in.qte_sell,
            added_by = added_by,

        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    @classmethod
    def update(cls,db:Session,obj_in:schemas.SellProductUpdate,added_by:str):
        db_obj = cls.get_by_uuid(db=db,uuid=obj_in.uuid)
        if not db_obj:
            raise HTTPException(status_code=404,detail="product_sold not found")
        db_obj.client_uuid = obj_in if obj_in.client_uuid else db_obj.client_uuid,
        db_obj.product_uuid = obj_in if obj_in.product_uuid else db_obj.product_uuid,
        db_obj.added_by = added_by
        db_obj.qte_sell = obj_in if obj_in.qte_sell else db_obj.qte_sell,


    @classmethod
    def get_many(
        cls,
        db:Session,
        page: int = 1,
        per_page: int = 25,
    ):
        record_query = db.query(models.SellProduct).filter(models.SellProduct.is_deleted==False)

        total = record_query.count()
        record_query = record_query.offset((page - 1) * per_page).limit(per_page)
        return schemas.SellProductResponseList(
            total = total,
            pages = math.ceil(total / per_page),
            per_page = per_page,
            current_page = page,
            data = record_query
        )



        
sell_product = CRUDsell_product(models.SellProduct)