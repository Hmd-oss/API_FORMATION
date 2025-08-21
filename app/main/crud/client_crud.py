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

class CRUDclient(CRUDBase[models.Client,schemas.ClientCreate,schemas.ClientUpdate]):

    @classmethod
    def get_by_uuid(cls,db:Session,uuid:str):
        return db.query(models.Client).filter(models.Client.uuid==uuid,models.Client.is_deleted==False).first()
    
    @classmethod
    def get_by_email(cls,db:Session,email:str):
        return db.query(models.Client).filter(models.Client.email==email,models.Client.is_deleted==False)
    

    @classmethod
    def get_by_phone_number(cls,db:Session,phone_number:str):
        return db.query(models.Client).filter(models.Client.phone_number==phone_number,models.Client.is_deleted==False).first()
    
    @classmethod
    def get_by_phone_number2(cls,db:Session,phone_number2:str):
        return db.query(models.Client).filter(models.Client.phone_number2==phone_number2,models.Client.is_deleted==False).first()
    

   
    @classmethod
    def delete(cls,db:Session,uuid:str):
        db_obj=cls.get_by_uuid(db=db,uuid=uuid)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Client not found")
        db.delete(db_obj)
        db.commit()


    @classmethod
    def soft_delete(cls,db:Session,uuid:str):
        db_obj=cls.get_by_uuid(db==db,uuid==uuid)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Client not found")
        db_obj.is_deleted=True
        db.commit()

    @classmethod
    def create(cls,db:Session,obj_in:schemas.ClientCreate):
        db_obj=models.Client(
            uuid=str(uuid.uuid4()),
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
            phone_number=obj_in.phone_number,
            phone_number2=obj_in.phone_number2,
            country=obj_in.country,
            city=obj_in.city,
            additional=obj_in.additional,

        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    @classmethod
    def update(cls,db:Session,obj_in:schemas.ClientUpdate):
        db_obj = cls.get_by_uuid(db=db,uuid=obj_in.uuid)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Client not found")
        
        db_obj.first_name = obj_in if obj_in.first_name else db_obj.first_name
        db_obj.last_name = obj_in if obj_in.last_name else db_obj.last_name
        db_obj.email = obj_in if obj_in.email else db_obj.email
        db_obj.phone_number = obj_in if obj_in.phone_number else db_obj.phone_number
        db_obj.phone_number2 = obj_in if obj_in.phone_number2 else db_obj.phone_number2
        db_obj.country = obj_in if obj_in.country else db_obj.country
        db_obj.city = obj_in if obj_in.city else db_obj.city
        db_obj.additional = obj_in if obj_in.additional else db_obj.additional
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
client = CRUDclient(models.client)
