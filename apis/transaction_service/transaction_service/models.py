# apis/transaction_service/transaction_service/models.py
import uuid
from django.db import models
from django.utils import timezone

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
        ('transfer', 'Transfer'),
    )

    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_id = models.UUIDField()  # Using UUIDField to store account ID
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)
    note = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'transaction_service'

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"
