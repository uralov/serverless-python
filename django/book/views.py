import json

from rest_framework import views
from rest_framework.response import Response
from django.forms.models import model_to_dict

from book.models import Book
from book.serializers import BookSerializer


class MyView(views.APIView):
    def get(self, request, format=None):
        book = Book.objects.first()
        message = {
            'message': 'Execution started successfully!'
        }
        return Response({
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(model_to_dict(book))
        })
