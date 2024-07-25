# apis/account_service/account_service/models.py
from django.db import models
from django.utils import timezone

class Account(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    account_holder = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'account_service'

    def __str__(self):
        return f"{self.account_holder} - {self.account_number}"
