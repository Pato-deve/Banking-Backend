from django.db import models
from customers.models import Customer

class Loan(models.Model):
    LOAN_TYPE_CHOICES = [
        ('Personal', 'Personal'),
        ('Hipotecario', 'Hipotecario'),
        ('Prendario', 'Prendario'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=50, choices=LOAN_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.loan_type} - ${self.amount}"