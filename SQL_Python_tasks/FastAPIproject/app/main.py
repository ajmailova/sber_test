from fastapi import FastAPI, HTTPException
from utils import get_all_tasks, add_task, delete_task_by_id
from pydantic import BaseModel, Field
from typing import List, Any

app = FastAPI()


# Модель для валидации данных
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Заголовок задачи не может быть пустым")
    completed: bool = False


# Модель для ответа
class TaskResponse(TaskCreate):
    id: int


@app.get("/")
def home_page():
    return {"message": "Backend для API-сервиса"}


# Получаем список задач
@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks():
    return get_all_tasks()


# Добавляем новую задачу в список
@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    try:
        new_task = add_task(task.title, task.completed)
        return new_task
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при добавлении задачи: {str(e)}")


# Удаляем задачу по её id
@app.delete("/tasks/{task_id}/", response_model=TaskResponse)
def delete_task(task_id: int):
    try:
        deleted_task = delete_task_by_id(task_id)
        if deleted_task:
            return deleted_task
        raise HTTPException(status_code=404, detail=f"Задача с id {task_id} не найдена")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при удалении задачи: {str(e)}")
