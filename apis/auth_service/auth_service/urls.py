# apis/auth_service/auth_service/urls.py
from django.urls import path
from .views import CustomTokenView

urlpatterns = [
    path('v1/auth/token/', CustomTokenView.as_view(), name='token'),
    path('v1/auth/token/validate/', CustomTokenView.as_view(), name='token_validation'),
]

