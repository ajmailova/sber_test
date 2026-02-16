from json_db_lite import JSONDatabase

# Путь к файлу с задачами
TASKS_FILE = 'tasks.json'

# Инициализация объекта
small_db = JSONDatabase(file_path=TASKS_FILE)


# Генерируем id
def generate_id():
    records = small_db.get_all_records()
    if not records:
        return 1
    return max(record.get('id', 0) for record in records) + 1


# Возвращаем все задачи из базы данных
def get_all_tasks():
    return small_db.get_all_records()
# Добавляем задачу
def add_task(title: str, completed: bool = False):
    # Генерируем новый уникальный id
    new_id = generate_id()

    # Создаем новую задачу
    new_task = {
        'id': new_id,
        'title': title.strip(),
        'completed': completed
    }

    # Добавляем в базу данных
    small_db.add_records(new_task)

    return new_task


# Удаляем задачу
def delete_task_by_id(task_id: int):
    # Получаем все записи для поиска
    records = small_db.get_all_records()

    # Ищем задачу по id
    deleted_task = None
    for record in records:
        if record.get('id') == task_id:
            deleted_task = record
            break

    # Если задача найдена, удаляем её
    if deleted_task:
        small_db.delete_record_by_key('id', task_id)
        return deleted_task

    return None
