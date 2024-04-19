import flet as ft
import sql_commands as sq

def main(page: ft.Page):

    #Инициализация
    page.title = "SQLite Viewer"
    global dbPATH
    plH1 = ft.CupertinoTextField(
            placeholder_text="users",
            bgcolor=ft.colors.WHITE24,
    )
    dbTable = ft.DataTable(
        columns=[
                ft.DataColumn(ft.Text("id")),
        ],    
    )

    #Функция для закрытия диалога
    def close_dlg(dialog):
        dialog.open = False
        page.update()

    #Функция для создания таблицы
    def create_table(e):
        table_name = plH1.value
        close_dlg(CreateTableDialog)

    #Диалог для создания таблицы
    CreateTableDialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Название таблицы:"),
        content=plH1,
        actions=[
            ft.TextButton("Отмена", on_click=lambda e: close_dlg(CreateTableDialog)),
            ft.TextButton("ОК", on_click=create_table),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Create table dialog was dismissed!"),
    )

    #Функция для открытия диалога
    def open_create_table_dialog(e):
        page.dialog = CreateTableDialog
        CreateTableDialog.open = True
        page.update()
    
    #Функция для импорта базы данных
    def import_db(e):

        pass
    
    #Кнопки
    CreateTableButton = ft.ElevatedButton(icon=ft.icons.TABLE_VIEW, text="Создать таблицу", on_click=open_create_table_dialog)
    AddColumnButton = ft.ElevatedButton(icon=ft.icons.VIEW_COLUMN, text="Добавить столбец")
    ImportDBButton = ft.ElevatedButton(icon=ft.icons.UPLOAD_FILE, text="Импорт", on_click=import_db)

    #Основная страница
    page.add(
        ft.Row(
            [
                ImportDBButton,
                CreateTableButton,
                AddColumnButton,
            ]
        ),
        dbTable,
    )

ft.app(target=main)
