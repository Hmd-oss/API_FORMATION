from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Client(BaseModel):
    first_name:str
    last_name:str
    email:str
    phone_number:str
    phone_number2:Optional[str]
    country:str
    city:str
    additional:Optional[str]

class ClientCreate(Client):
    pass

class ClientUpdate(BaseModel):
    uuid:str
    first_name:Optional[str]
    last_name:Optional[str]
    email:Optional[str]
    phone_number:Optional[str]
    phone_number2:Optional[str]
    country:Optional[str]
    city:Optional[str]
    additional:Optional[str]

class ClientDelete(BaseModel):
    uuid:str

class ClientResponse(BaseModel):
    uuid:str
    first_name:str
    email:str
    last_name:Optional[str]
    phone_number:str
    phone_number2:Optional[str]
    country:str
    city:str
    additional:Optional[str]
    is_active:bool
    created_at:datetime
    updated_at:Optional[datetime]

    model_config = ConfigDict(from_attributes=True)


class ClientSell(BaseModel):
    uuid:str
    first_name:str
    last_name:Optional[str]
    model_config = ConfigDict(from_attributes=True)