create_task = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_text TEXT
    )
"""

# CRUD - CREATE, READ, UPDATE, DELETE

insert_task = "INSERT INTO tasks (task_text) VALUES (?)"

select_task = 'SELECT id, task_text FROM tasks'

update_task = 'UPDATE tasks SET task_text = ? WHERE id = ?'

delete_task = 'DELETE FROM tasks WHERE id = ?'
