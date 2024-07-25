# apis/transaction_service/transaction_service/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer
from utilities.logger import Logger
from utilities.response_controller import ResponseController as Response
from utilities.permissions import AllowAnyWithToken

class TransactionView(APIView):
    permission_classes = [AllowAnyWithToken]

    def get(self, request, *args, **kwargs):
        logger = Logger()
        account_id = request.query_params.get('account_id')
        try:
            transactions = Transaction.objects.filter(account_id=account_id)
            serializer = TransactionSerializer(transactions, many=True)
            return Response.success("Transactions retrieved successfully", serializer.data)
        except Exception as e:
            error_id = logger.error(__file__, self.get.__name__, str(e))
            return Response.error(f'Internal server error, error_id: {error_id}', status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        logger = Logger()
        try:
            serializer = TransactionSerializer(data=request.data)
            if serializer.is_valid():
                transaction = serializer.save()
                return Response.success("Transaction successful", serializer.data, status.HTTP_201_CREATED)  # Updated status code
            return Response.error(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_id = logger.error(__file__, self.post.__name__, str(e))
            return Response.error(f'Internal server error, error_id: {error_id}', status.HTTP_500_INTERNAL_SERVER_ERROR)
