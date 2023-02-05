import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from api.models import Category, Genre, Title, GenresTitle


# from users.models import User


class Command(BaseCommand):
    """Команда для загрузки csv файлов в базу данных:
     python manage.py fill_database """

    help = 'Загрузка информации из csv файлов в базу данных'



    def fill_category(self):
        with open(os.path.join(settings.BASE_DIR, 'static/data/category.csv'),
                  'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[0] != 'id':
                    Category.objects.get_or_create(
                        id=row[0], name=row[1], slug=row[2]
                    )

    def fill_genre(self):
        with open(os.path.join(settings.BASE_DIR, 'static/data/genre.csv'),
                  'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[0] != 'id':
                    Genre.objects.get_or_create(
                        id=row[0], name=row[1], slug=row[2]
                    )

    def fill_titles(self):
        with open(os.path.join(settings.BASE_DIR, 'static/data/titles.csv'),
                  'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[0] != 'id':
                    Title.objects.get_or_create(
                        id=row[0], name=row[1], year=row[2], category_id=row[3]
                    )

    def fill_genre_title(self):
        with open(
            os.path.join(settings.BASE_DIR, 'static/data/genre_title.csv'),
            'r',
            encoding='utf-8'
        ) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[0] != 'id':
                    GenresTitle.objects.get_or_create(
                        id=row[0], title_id=row[1], genres_id=row[2]
                    )



    def handle(self, *args, **options):

        self.fill_category()
        self.fill_genre()
        self.fill_titles()
        self.fill_genre_title()

