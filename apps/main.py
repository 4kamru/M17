#ДЗ_17-1
# from fastapi import FastAPI, Request, HTTPException, Path
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel
# from fastapi.templating import Jinja2Templates
# from typing import Annotated, List

# В файле main.py создайте сущность FastAPI(), напишите один маршрут для неё - '/', по которому функция
# возвращает словарь - {"message": "Welcome to Taskmanager"}.
# Импортируйте объекты APIRouter и подключите к ранее созданному приложению FastAPI, объединив все
# маршруты в одно приложение.

from fastapi import FastAPI
from routers import task, user

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}


app.include_router(task.router)
app.include_router(user.router)

# python3 -m uvicorn main:apps