from db import main_db
import flet as ft 


def main(page: ft.Page):
    page.title = 'Todo list'
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column()
    
    filter_type = 'all'

    def load_tasks():
        task_list.controls.clear()
        for task_id, task_text, completed in main_db.get_tasks(filter_type):
            task_list.controls.append(view_task(task_id=task_id, task_text=task_text, completed=completed))

    def view_task(task_id, task_text, completed=None):
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)

        checkbox_task = ft.Checkbox(value=bool(completed), on_change=lambda e: toggle_task(task_id=task_id, is_completed=e.control.value))

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

        return ft.Row([checkbox_task, task_field, edit_button, save_button])
    
    def toggle_task(task_id, is_completed):
        print(is_completed)
        main_db.update_task(task_id=task_id, completed=int(is_completed))
        print(int(is_completed))
        load_tasks()

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

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_tasks()
    
    filter_buttons = ft.Row([
        ft.ElevatedButton('Все задачи', on_click=lambda e: set_filter('all')),
        ft.ElevatedButton('Не готово', on_click=lambda e: set_filter('uncompleted')),
        ft.ElevatedButton('Готово', on_click=lambda e: set_filter('completed'))
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    page.add(main_objects, filter_buttons, task_list)
    load_tasks()


if __name__ == "__main__":
    main_db.init_db()
    ft.run(main)