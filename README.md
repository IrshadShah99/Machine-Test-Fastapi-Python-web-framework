# Machine-Test-Fastapi-Python-web-framework
---

# 🛒 Category and Product Project

A simple **FastAPI-based web application** that manages categories and products with a MySQL database backend. This project demonstrates how to build a RESTful API using FastAPI, SQLAlchemy, and Pydantic.

---

## 📂 Project Structure
- `database.py` → Database connection setup  
- `main.py` → Application entry point  
- `models.py` → SQLAlchemy models for Category & Product  
- `schemas.py` → Pydantic schemas for request/response validation  
- `requirements.txt` → Dependencies  

---

## ⚙️ Tech Stack
- **Backend:** FastAPI  
- **Database:** MySQL  
- **ORM:** SQLAlchemy  
- **Validation:** Pydantic  
- **Server:** Uvicorn  

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Create database
```sql
create database test_db;
```

### 3. Run the project
```bash
uvicorn main:app --reload
```

### 4. Test endpoints
Open interactive API docs at:  
👉 `http://127.0.0.1:8000/docs` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fdocs")

---

## 📌 Features
- Create, read, update, and delete categories  
- Manage products linked to categories  
- Interactive Swagger UI for testing endpoints  
- Modular project structure for scalability  
