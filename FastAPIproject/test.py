import requests

BASE_URL = "http://127.0.0.1:8000"


def get_tasks():
    response = requests.get(f"{BASE_URL}/tasks/")
    return response.json()


def create_task(title: str, completed: bool = False):
    response = requests.post(
        f"{BASE_URL}/tasks/",
        json={"title": title, "completed": completed}
    )
    return response.json()


def dell_task(task_id: int):
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}/")
    return response.json()


tasks = get_tasks()
for i in tasks:
    print(i)
new_task = create_task("Тест", False)
print(f'Задача создана:{new_task}')

tasks = get_tasks()
for i in tasks:
    print(f'Список новых задач:{i}')

task_id_to_delete = tasks[-1]['id']
result = dell_task(task_id_to_delete)
print(f'Удалена задача:{result}')

