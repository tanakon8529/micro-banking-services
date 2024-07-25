
# apis/transaction_service/transaction_service/urls.py
from django.urls import path
from .views import TransactionView

urlpatterns = [
    path('v1/transactions/', TransactionView.as_view(), name='transactions'),
]
