from dataclasses import dataclass
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.json import JSONB
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Boolean
from sqlalchemy import event
from app.main.models.db.base_class import Base
from enum import Enum

class Client(Base):

    __tablename__="clients"
    uuid = Column(String,primary_key=True,index=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    phone_number = Column(String,unique=True,nullable=False)
    phone_number2 = Column(String,unique=True,nullable=True)
    country = Column(Text,nullable=True)
    city = Column(Text,nullable=True)
    additional = Column(Text,nullable=True)
    is_active = Column(Boolean,default=False)
    is_deleted = Column(Boolean,default=False)
    created_at = Column(DateTime,default=func.now())
    updated_at = Column(DateTime,default=func.now(),onupdate=func.now())