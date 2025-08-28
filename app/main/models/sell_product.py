from dataclasses import dataclass
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.json import JSONB
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Boolean
from sqlalchemy import event
from app.main.models.db.base_class import Base
from enum import Enum


class SellProduct(Base):
    __tablename__ = "sell_products"

    uuid = Column(String, primary_key=True, unique=True)

    client_uuid = Column(String, ForeignKey("clients.uuid"), nullable=False)
    client = relationship("Client",foreign_keys=[client_uuid],backref="sell_products")

    product_uuid = Column(String, ForeignKey("products.uuid"), nullable=False, index=True)
    product = relationship("Product",foreign_keys=[product_uuid],backref="sell_products")
    
    added_by = Column(String,ForeignKey("users.uuid"),nullable=False, index=True)
    creator = relationship("User",foreign_keys=[added_by],backref="sell_products")

    qte_sell = Column(Integer, nullable=False)
    is_active = Column(Boolean,default=False)

    is_deleted = Column(Boolean,default=False)
    created_at = Column(DateTime,default=func.now())
    updated_at = Column(DateTime,default=func.now(),onupdate=func.now())