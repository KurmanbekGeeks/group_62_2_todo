create_task = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_text TEXT,
        completed INTEGER DEFAULT 0 
    )
"""

# CRUD - CREATE, READ, UPDATE, DELETE

insert_task = "INSERT INTO tasks (task_text) VALUES (?)"

select_task = 'SELECT id, task_text, completed FROM tasks'

select_task_completed = "SELECT id, task_text, completed FROM tasks WHERE completed = 1 "
select_task_uncompleted = "SELECT id, task_text, completed FROM tasks WHERE completed = 0 "

update_task = 'UPDATE tasks SET task_text = ? WHERE id = ?'

delete_task = 'DELETE FROM tasks WHERE id = ?'
