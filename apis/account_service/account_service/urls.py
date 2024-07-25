
# apis/account_service/account_service/urls.py
from django.urls import path
from .views import AccountView

urlpatterns = [
    path('v1/accounts/', AccountView.as_view(), name='accounts'),
]
