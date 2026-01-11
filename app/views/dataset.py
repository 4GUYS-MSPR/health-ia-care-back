import json

from pydantic import ValidationError
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, JSONParser

from app.models.exercice import ExerciceScheme

class DataImportViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    parser_classes = [MultiPartParser, JSONParser]

    def create(self, request):
        file = request.FILES.get('file')

        if not file and not request.data:
            return Response(
                {"detail": "No data"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        data = request.data
        if not isinstance(data, list):
            data = [data]
        
        errors = []
        valid_data = []
        
        for index, item in enumerate(data):
            try:
                scheme = ExerciceScheme(**item)
                valid_data.append(scheme.model_dump_json())
            except ValidationError as e:
                errors.append(e.json())

        return Response({"errors": errors, "data": valid_data}, status=status.HTTP_200_OK)
