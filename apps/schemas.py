#schemas.py
# Создайте 4 схемы в модуле schemas.py, наследуемые от BaseModel, для удобной работы с будущими объектами БД:
# 1. CreateUser с атрибутами: username(str), firstname(str), lastname(str) и age(int)
# 2. UpdateUser с атрибутами: firstname(str), lastname(str) и age(int)
# 3. CreateTask с атрибутами: title(str), content(str), priority(int)
# 4. UpdateTask с теми же атрибутами, что и CreateTask.
# Обратите внимание, что 1/2 и 3/4 схемы обладают одинаковыми атрибутами.

from pydantic import BaseModel

# классы (схемы) для объектов пользователя
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int


# классы (схемы) для объектов задач

class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int