import sqlite3
from config import path_db
from db import queries


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.create_task)
    conn.commit()
    conn.close()


def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_task, (task, ))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id 


def get_tasks(filter_type):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if filter_type == 'all':
        cursor.execute(queries.select_task)
    elif filter_type == 'completed':
        cursor.execute(queries.select_task_completed)
    elif filter_type == 'uncompleted':
        cursor.execute(queries.select_task_uncompleted)

    tasks = cursor.fetchall()
    conn.close()
    return tasks 


def update_task(task_id, new_task_text=None, completed=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if new_task_text is not None:
        cursor.execute(queries.update_task, (new_task_text, task_id))
    elif completed is not None:
        cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (completed, task_id))
    conn.commit()
    conn.close()

