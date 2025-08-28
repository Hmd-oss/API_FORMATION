from typing import Optional
from app.main.schemas.user import AddedBySlim
from app.main.schemas.product import ProductSell
from app.main.schemas.client import ClientSell
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class SellProductBase(BaseModel):
    client_uuid: str
    product_uuid: str
    qte_sell: int 

class SellProductCreate(SellProductBase):
    pass

class SellProductUpdate(BaseModel):
    uuid: str
    client_uuid: Optional[str]=None
    product_uuid: Optional[str]=None
    qte_sell: Optional[int] 
    

class SellProductDelete(BaseModel):
    uuid:str


class SellProductResponse(BaseModel):
    uuid: str
    client : ClientSell
    product: ProductSell
    creator: AddedBySlim
    qte_sell: int
    created_at: datetime
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)



class SellProductResponseList(BaseModel):
    total:int
    pages:int
    per_page:int
    current_page:int
    data:list[SellProductResponse]
    model_config = ConfigDict(from_attributes=True)
