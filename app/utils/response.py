from rest_framework import status
from rest_framework.response import Response

class JsonResponse:

    @staticmethod
    def errors(errors):
        return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def success(data):
        return Response(data, status=status.HTTP_200_OK)

    @staticmethod
    def response(data: dict, code: int):
        return Response(data, status=code)
