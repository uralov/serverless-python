from django.db import models


class BookDjango(models.Model):
    name = models.CharField('name', max_length=20)

    class Meta:
        db_table = 'book_book'
