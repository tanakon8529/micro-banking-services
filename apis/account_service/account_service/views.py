# apis/account_service/account_service/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Account
from .serializers import AccountSerializer
from utilities.logger import Logger
from utilities.response_controller import ResponseController as Response
from utilities.permissions import AllowAnyWithToken

class AccountView(APIView):
    permission_classes = [AllowAnyWithToken]

    def get(self, request, *args, **kwargs):
        logger = Logger()
        try:
            accounts = Account.objects.all()
            serializer = AccountSerializer(accounts, many=True)
            return Response.success("Accounts retrieved successfully", serializer.data)
        except Exception as e:
            error_id = logger.error(__file__, self.get.__name__, str(e))
            return Response.error(f'Internal server error, error_id: {error_id}', status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        logger = Logger()
        try:
            serializer = AccountSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response.success("Account created successfully", serializer.data, status=status.HTTP_201_CREATED)
            return Response.error(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_id = logger.error(__file__, self.post.__name__, str(e))
            return Response.error(f'Internal server error, error_id: {error_id}', status.HTTP_500_INTERNAL_SERVER_ERROR)
