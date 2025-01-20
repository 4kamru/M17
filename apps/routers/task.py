# В модуле task.py напишите APIRouter с префиксом '/task' и тегом 'task', а также следующие маршруты, с пустыми функциями:
# 1. get '/' с функцией all_tasks.
# 2. get '/task_id' с функцией task_by_id.
# 3. post '/create' с функцией create_task.
# 4. put '/update' с функцией update_task.
# 5. delete '/delete' с функцией delete_task

from fastapi import APIRouter

router = APIRouter(prefix='/task',tags=['task'])

@router.get('/')
async def all_tasks():
    pass

@router.get('/task_id')
async def create_task():
    pass

@router.post('/create')
async def create_task():
    pass

@router.put("/update")
async def update_task():
    pass


@router.delete("/delete")
async def delete_task():
    pass