from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
import flet as ft

from config import config
from tasks.todo_app import TodoApp


def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.update()

    # create application instance
    app = TodoApp()

    # add application's root control to the page
    page.add(app)


class Command(BaseCommand):
    help = 'Import old tools and calibrations'

    # def add_arguments(self, parser):
    #     parser.add_argument('db', type=str, default="old", required=False)

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.MIGRATE_HEADING('Let run flutter app.'))
            ft.app(target=main, port=config.APP_PORT, view=ft.FLET_APP_HIDDEN, host=config.APP_HOST)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Flutter app error: {e}'))
        self.stdout.write(self.style.SUCCESS('Finish running flutter app.'))


def parse_date(date_txt: str):
    try:
        return datetime.strptime(date_txt, "%d.%m.%Y %H:%M:%S")
    except Exception as e:
        return e
