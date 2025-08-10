# Pet-project-PDH-
PDH is a personal tracking and data analysis system where you can import data from various sources (steps, sleep, expenses, tasks, weather, social media API, etc.), store them in a database and analyze


This is backend application on **FastAPI** and **PostgreSQL** for storing and processing personal data.  
The project implements registration, authorization (JWT), CRUD operations with data, and launch via Docker.

---

## 📂 Стек технологий
- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Docker / Docker Compose
- JWT авторизация

---

## 📜 Фичи MVP
- Регистрация и авторизация пользователей
- Хранение данных в PostgreSQL
- CRUD API для работы с данными
- JWT-токены для аутентификации
- Запуск в контейнерах через Docker

---

## 🚀 Установка и запуск

### 1. Клонировать репозиторий

git clone https://github.com/username/pdh-backend.git

cd pdh-backend

### 2. Запуск с Docker

docker-compose up --build

После запуска API будет доступна по адресу:
[https://localhost:8000/docs](http://localhost:8000/docs)

<br><br>

###### 10.08.2025
