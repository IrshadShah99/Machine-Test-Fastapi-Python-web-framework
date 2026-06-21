from pydantic import BaseModel
from typing import Optional

# Class for Category
class CreateCategory(BaseModel):
    name:str
    summary:str

    class Config:
        from_attributes=True 

class ResponseCategory(BaseModel):
    id:int
    name:str
    summary:str

    class Config:
        from_attributes=True

# Class for Products
class CreateProduct(BaseModel):
    name:str
    prod_price:int
    cat_id:int

    class Config:
        from_attributes=True

class ResponseProduct(BaseModel):
    id:int
    name:str
    prod_price:int
    cat_id:int
    relation_cat:Optional[ResponseCategory]=None

    class Config:
        from_attributes=True
