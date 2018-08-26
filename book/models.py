from django.db import models


class Book(models.Model):
    name = models.CharField('name', max_length=20)
