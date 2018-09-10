import json
import os

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()

from conf.models import BookDjango


def hello_django_orm(event, context):
    book = BookDjango.objects.first()
    response = {
        "statusCode": 200,
        "body": json.dumps({'id': book.id, 'name': book.name})
    }

    return response
