# Machine Test : Fastapi Python web framework
## Title : Category and Product Project

Project Structure:
database.py
main.py
models.py
schemas.py
requirements.txt 

Tech Stack Used:
Backend : Fastapi
Database : MySQL

### install requirements.txt file
pip install -r requirements.txt

### create database in MySQL Workbench
create database test_db;

### Use command to run this project
uvicorn main:app --reload

### Test all endpoints 
http://127.0.0.1:8000/docs
