from rest_framework.response import Response
from rest_framework import status

class ResponseController:
    @staticmethod
    def success(message, data=None, status=status.HTTP_200_OK):
        return Response({"details": message, "data": data}, status=status)

    @staticmethod
    def error(message, status=status.HTTP_400_BAD_REQUEST):
        return Response({"details": message, "data": None}, status=status)