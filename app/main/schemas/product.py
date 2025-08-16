from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Product(BaseModel):
    name:str
    price:float
    quantity:float
    pu:float
    pa:float
    stock_limit:float


class ProductCreate(Product):
    pass

class ProductUpdated(BaseModel):
    uuid:str
    name:Optional[str]
    price:Optional[float]
    quantity:Optional[float]
    pu:Optional[float]
    pa:Optional[float]
    stock_limit:Optional[float]

class ProductDeleted(BaseModel):
    uuid:str


class ProductResponse(BaseModel):
    uuid:str
    name:str
    price:float
    quantity:float
    pu:float
    pa:float
    stock_limit:float
    is_active:bool
    created_at:datetime
    updated_at:Optional[datetime]

    