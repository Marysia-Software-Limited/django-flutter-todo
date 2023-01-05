from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
import flet as ft

from tasks.models import Task


def main(page: ft.Page):
    # def add_clicked(e):
    #     page.add(ft.Checkbox(label=new_task.value))
    #     new_task.value = ""
    #     page.update()

    # new_task = ft.TextField(hint_text="Whats needs to be done?")

    # page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked))

    columns = []
    fields = [
        ("name", "Zadanie",),
        ("is_done", "Zrobione"),
        ("date_add", "Data dodania")
    ]

    for field, label in fields:
        columns.append(ft.DataColumn(
                    ft.Text(label),
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ))

    rows = []

    for task in Task.objects.all():
        row = []
        for field, label in fields:
            row.append(ft.DataCell(ft.Text(getattr(task, field, ""))))
        rows.append(ft.DataRow(row))


    page.add(
        ft.DataTable(
            # width=700,
            bgcolor="yellow",
            border=ft.border.all(2, "red"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(3, "blue"),
            horizontal_lines=ft.border.BorderSide(1, "green"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=100,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=200,
            columns=columns,
            rows=rows,
        ),
    )


class Command(BaseCommand):
    help = 'Import old tools and calibrations'

    # def add_arguments(self, parser):
    #     parser.add_argument('db', type=str, default="old", required=False)

    def handle(self, *args, **options):
            try:
                self.stdout.write(self.style.MIGRATE_HEADING('Let run flutter app.'))
                ft.app(target=main)
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Flutter app error: {e}'))
            self.stdout.write(self.style.SUCCESS('Finish running flutter app.'))


def parse_date(date_txt: str):
    try:
        return datetime.strptime(date_txt, "%d.%m.%Y %H:%M:%S")
    except Exception as e:
        return e
