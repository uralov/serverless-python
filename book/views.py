import json

from rest_framework import views
from rest_framework.response import Response


class MyView(views.APIView):
    def get(self, request, format=None):
        message = {
            'message': 'Execution started successfully!'
        }
        return Response({
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(message)
        })
