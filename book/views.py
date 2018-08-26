from rest_framework import views
from rest_framework.response import Response

from book.models import Book
from book.serializers import BookSerializer


class MyView(views.APIView):
    def get(self, request, format=None):
        book = Book.objects.first()

        return Response({
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': BookSerializer(book).data
        })
