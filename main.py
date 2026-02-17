from db import main_db
import flet as ft 


def main(page: ft.Page):
    page.title = 'Todo list'
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column()

    def load_tasks():
        task_list.controls.clear()
        for task_id, task_text in main_db.get_tasks():
            task_list.controls.append(view_task(task_id=task_id, task_text=task_text))

    def view_task(task_id, task_text):
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)

        def enable_edit(_):
            if task_field.read_only == True:
                task_field.read_only = False
            else:
                task_field.read_only = True

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)

        def save_task(_):
            main_db.update_task(task_id=task_id, new_task_text=task_field.value)
            task_field.read_only = True


        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)

        return ft.Row([task_field, edit_button, save_button])

    def add_task_db(_):
        if text_input.value:
            task = text_input.value
            task_id = main_db.add_task(task=task)
            print(f'Задача {task} успешно записали! ID - {task_id}')

            task_list.controls.append(view_task(task_id=task_id, task_text=task))

            text_input.value = None


    text_input = ft.TextField(label='Введите задачу', expand=True, on_submit=add_task_db)
    send_button = ft.IconButton(icon=ft.Icons.SEND, on_click=add_task_db)


    main_objects = ft.Row([text_input, send_button])

    page.add(main_objects, task_list)
    load_tasks()


if __name__ == "__main__":
    main_db.init_db()
    ft.run(main)