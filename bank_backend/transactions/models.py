from django.db import models
from customers.models import Customer

class Transaction(models.Model):
    transaction_type = models.ForeignKey('TransactionType', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.transaction_type} - ${self.amount}"

class TransactionType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name