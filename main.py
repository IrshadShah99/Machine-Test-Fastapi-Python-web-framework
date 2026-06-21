from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import session_handler,db_engine,Base
# import from models.py
from models import Category_tb,Product_tb
# import from schemas.py
from schemas import CreateCategory,CreateProduct

app = FastAPI()
Base.metadata.create_all(bind=db_engine)

# database dependency
def get_db_instance():
    db = session_handler()
    try:
        yield db
    finally:
        db.close()

# fastapi 
@app.get("/")
def api_checking():
    return{"msg":"Category and Product api running successfully"}

# 1) Category CRUD Operations

@app.get("/api/categories")
def get_category_detail(page:int=1,db:Session=Depends(get_db_instance)):
    limit=5
    offset = (page-1)*limit
    categories = db.query(Category_tb).offset(offset).limit(limit).all()
    return categories

@app.post("/api/categories")
def create_category_detail(category:CreateCategory,db:Session=Depends(get_db_instance)):
    category_info = Category_tb(name=category.name,summary=category.summary)
    db.add(category_info)
    db.commit()
    db.refresh(category_info)
    return category_info

@app.get("/api/categories/{id}")
def get_category_info(id:int,db:Session=Depends(get_db_instance)):
    cat_detail = db.query(Category_tb).filter(Category_tb.id==id).first()
    if not cat_detail:
        return {"Error":"Category details not found"}
    return cat_detail

@app.put("/api/categories/{id}")
def update_category_info(id:int,category:CreateCategory,db:Session=Depends(get_db_instance)):
    existing = db.query(Category_tb).filter(Category_tb.id==id).first()
    if not existing:
        return {"Error":"Category detail not found"}
    existing.name = category.name
    existing.summary = category.summary
    db.commit()
    db.refresh(existing)
    return existing

@app.delete("/api/categories/{id}")
def delete_category_info(id:int,db:Session=Depends(get_db_instance)):
    category = db.query(Category_tb).filter(Category_tb.id == id).first()
    if not category:
        return {"Error":"Category detail not found"}
    db.delete(category)
    db.commit()
    return {"msg":"Category deleted successfully"}

# 2) Product CRUD Operations
@app.get("/api/products")
def get_product_detail(page:int=1,db:Session=Depends(get_db_instance)):
    limit=5
    offset=(page-1)*limit
    products = db.query(Product_tb).offset(offset).limit(limit).all()
    return products

@app.post("/api/products")
def create_product_data(product:CreateProduct,db:Session=Depends(get_db_instance)):
    category = db.query(Category_tb).filter(Category_tb.id==product.cat_id).first()
    if not category:
        return {"Error": "Category detail not found"}
    product_data = Product_tb(name=product.name,prod_price=product.prod_price,cat_id=product.cat_id)
    db.add(product_data)
    db.commit()
    db.refresh(product_data)
    return product_data

@app.get("/api/products/{id}")
def get_product_data(id:int,db:Session=Depends(get_db_instance)):
    product=db.query(Product_tb).filter(Product_tb.id == id).first()
    if not product:
        return {"Error":"Product data not found"}
    return{"id":product.id,"name":product.name,"prod_price":product.prod_price,"category":{"id":product.relation_cat.id,"name":product.relation_cat.name,"summary":product.relation_cat.summary}}

@app.put("/api/products/{id}")
def update_product_data(id:int,product:CreateProduct,db:Session=Depends(get_db_instance)):
    existing=db.query(Product_tb).filter(Product_tb.id == id).first()
    if not existing:
        return {"Error":"Product data not found"}
    existing.name=product.name
    existing.prod_price=product.prod_price
    existing.cat_id=product.cat_id
    db.commit()
    db.refresh(existing)
    return existing

@app.delete("/api/products/{id}")
def delete_product_data(id:int,db:Session=Depends(get_db_instance)):
    product = db.query(Product_tb).filter(Product_tb.id==id).first()
    if not product:
        return {"Error":"Product data not found"}
    db.delete(product)
    db.commit()
    return {"msg":"Product data deleted successfully"} 