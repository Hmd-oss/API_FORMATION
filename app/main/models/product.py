from dataclasses import dataclass
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.json import JSONB
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Boolean,Float
from sqlalchemy import event
from app.main.models.db.base_class import Base
from enum import Enum



class Product(Base):
   __tablename__ = "products"
   uuid = Column(String,primary_key=True,index=True)
   name = Column(String,unique=True,nullable=False)
   quantity = Column(Float,unique=True,nullable=False)
   pu = Column(Float,unique=True,nullable=False)
   pa = Column(Float,unique=True,nullable=False)
   stock_limit = Column(Float,unique=True,nullable=False)
   is_active = Column(Boolean,default=False)
   is_deleted = Column(Boolean,default=False)
   created_at = Column(DateTime, default=func.now())  # Account creation timestamp
   updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Last update timestamp

