from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_user="root"
db_pass="Dan%409028"  # MySql workbench password : %40 is written instead of @ bcz @ gives error
db_host="localhost"
db_port="3306"
db_name="test_db"

db_conn_url="mysql+pymysql://"+db_user+":"+db_pass+"@"+db_host+":"+db_port+"/"+db_name

db_engine=create_engine(db_conn_url)
session_handler=sessionmaker(bind=db_engine)
Base=declarative_base()