from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Class for Category
class Category_tb(Base):
    __tablename__ = "cat_info"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(220),nullable=False)
    summary = Column(String(220))
    relation_prod = relationship("Product_tb",back_populates="relation_cat")

# Class for Products
class Product_tb(Base):
    __tablename__ = "prod_data"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),nullable=False)
    prod_price = Column(Integer)
    cat_id = Column(Integer,ForeignKey("cat_info.id")) 
    relation_cat = relationship("Category_tb",back_populates="relation_prod")
